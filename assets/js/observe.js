/**
 * observe.html — Are.na meta-archive 인벤토리 탐색
 * 데이터: data/arena/inventory-enriched.json
 */

const FACET_AXES = [
  { key: 'operator', label: '운영 주체' },
  { key: 'unit', label: '수집 단위' },
  { key: 'form_experiment', label: '형식 실험' },
  { key: 'navigation', label: '탐색' },
  { key: 'stack', label: '스택', hideValues: ['unknown'] },
  { key: 'locale', label: '지역·언어', array: true },
  { key: 'group', label: '1차 그룹', top: true },
];

const AXIS_LABELS = {
  institution: '기관',
  community: '커뮤니티',
  individual: '개인',
  hybrid: '혼합',
  corporate: '상업',
  item: '유물',
  text: '글',
  event: '사건',
  place: '장소',
  aggregate: '집계',
  high: '높음',
  medium: '중간',
  low: '낮음',
  explicit: '명시',
  implicit: '암묵',
  denied: '거부',
  open: '개방',
  gated: '제한',
  hidden: '숨김',
  defunct: '폐쇄',
  taxonomy: '분류',
  search: '검색',
  chronology: '연대',
  spatial: '공간',
  associative: '연결',
  none: '없음',
  published: '발행',
  in_progress: '진행',
  none_critique: '미작성',
};

let data = null;
const active = new Map();
let sortBy = 'inventory_id';
let showCritiqueCandidates = false;

function hasCritique(item) {
  return item.critique.status !== 'none';
}

function critiquedCount(fc) {
  const c = fc.critique || {};
  return (c.published ?? 0) + (c.in_progress ?? 0) + (c.planned ?? 0);
}

function label(val) {
  return AXIS_LABELS[val] || val;
}

function shortGroup(name) {
  const map = {
    '형식이 곧 내용인 아카이브': '형식=내용',
    '분류 체계가 독특한 아카이브': '분류',
    '대규모 통합 플랫폼': '통합',
    '정부·공공 웹 아카이브': '웹아카이브',
    '기관 아카이브': '기관',
    '한국 공공·지역·역사 아카이브': '한국',
    '페미니스트·사회운동·대안 아카이브': '대안',
    '개인 아카이브·포트폴리오': '개인',
    '예술가 출판·독립 플랫폼': '출판',
    '디자인·시각 아카이브': '디자인',
    '잡지·미디어 아카이브': '미디어',
    '웹 역사·디지털 유산': '웹역사',
    '디자인 영감·레퍼런스 (경계)': '경계',
    '접근 불가·미확인': '미확인',
  };
  return map[name] || name;
}

function normNav(v) {
  if (Array.isArray(v)) return v;
  return v ? [v] : [];
}

function itemValue(item, axis) {
  if (axis.top) return item[axis.key];
  if (axis.field) return item[axis.topKey || axis.key]?.[axis.field];
  const v = item.axes?.[axis.key];
  if (axis.array) {
    if (Array.isArray(v)) return v;
    if (typeof v === 'string') return [v];
    return [];
  }
  return v;
}

function matchesFacets(item) {
  for (const [axisKey, values] of active) {
    const axis = FACET_AXES.find((a) => a.key === axisKey);
    const raw = itemValue(item, axis);
    const vals = axis?.array && Array.isArray(raw) ? raw : normNav(raw);
    const flat = Array.isArray(vals) ? vals : [vals];
    if (!flat.some((v) => values.has(v))) return false;
  }
  return true;
}

function getFiltered() {
  const q = document.getElementById('search').value.trim().toLowerCase();
  const onlyCritique = document.getElementById('only-critique').checked;
  const onlyYaml = document.getElementById('only-yaml').checked;

  let items = data.items.filter((item) => {
    if (onlyCritique && !hasCritique(item)) return false;
    if (showCritiqueCandidates && hasCritique(item)) return false;
    if (onlyYaml && !item.has_manual_yaml) return false;
    if (q) {
      const hay = `${item.inventory_id} ${item.title} ${item.url}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return matchesFacets(item);
  });

  if (sortBy === 'connected') {
    items = items.slice().sort((a, b) => (b.connected || '').localeCompare(a.connected || ''));
  } else if (sortBy === 'inventory_id') {
    items = items.slice().sort((a, b) => a.inventory_id.localeCompare(b.inventory_id));
  } else {
    items = items.slice().sort((a, b) => a.title.localeCompare(b.title, 'ko'));
  }
  return items;
}

function renderStats() {
  const fc = data.facet_counts;
  const el = document.getElementById('stats');
  const cards = [
    { n: data.total, label: '전체' },
    { n: fc.form_experiment?.high ?? 0, label: '형식 high' },
    { n: fc.operator?.institution ?? 0, label: '기관' },
    { n: fc.operator?.community ?? 0, label: '커뮤니티' },
    { n: critiquedCount(fc), label: '비평' },
    { n: data.manual_yaml_count, label: 'YAML' },
  ];
  el.innerHTML = cards
    .map((c) => `<div class="observe-stat"><span class="n">${c.n}</span><span class="l">${c.label}</span></div>`)
    .join('');
}

function renderActiveFilters() {
  const el = document.getElementById('active-filters');
  const parts = [];
  for (const [axisKey, values] of active) {
    const axis = FACET_AXES.find((a) => a.key === axisKey);
    values.forEach((v) => parts.push(`${axis?.label || axisKey}: ${label(v)}`));
  }
  if (document.getElementById('only-critique').checked) parts.push('비평');
  if (showCritiqueCandidates) parts.push('비평 후보');
  if (document.getElementById('only-yaml').checked) parts.push('YAML');
  const q = document.getElementById('search').value.trim();
  if (q) parts.push(`검색: ${q}`);

  el.hidden = !parts.length;
  el.textContent = parts.length ? `필터: ${parts.join(' · ')}` : '';
}

function renderFacets() {
  const el = document.getElementById('facets');
  el.innerHTML = '';
  FACET_AXES.forEach((axis) => {
    const counts = data.facet_counts[axis.key] || {};
    let entries = Object.entries(counts).sort((a, b) => b[1] - a[1]);
    if (axis.hideValues) {
      entries = entries.filter(([val]) => !axis.hideValues.includes(val));
    }
    if (!entries.length) return;

    const group = document.createElement('div');
    group.className = 'observe-facet-group';
    group.innerHTML = `<h3>${axis.label}</h3>`;
    const chips = document.createElement('div');
    chips.className = 'chips';

    entries.forEach(([val, n]) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'chip' + (active.get(axis.key)?.has(val) ? ' active' : '');
      btn.innerHTML = `${label(val)}<span class="count">${n}</span>`;
      btn.addEventListener('click', () => {
        if (!active.has(axis.key)) active.set(axis.key, new Set());
        const set = active.get(axis.key);
        if (set.has(val)) set.delete(val);
        else set.add(val);
        if (!set.size) active.delete(axis.key);
        document.querySelectorAll('.preset').forEach((p) => p.classList.remove('active'));
        renderFacets();
        renderList();
      });
      chips.appendChild(btn);
    });
    group.appendChild(chips);
    el.appendChild(group);
  });
}

const SITE = 'https://meta-archives.xyz';

function critiqueBadge(critique) {
  const { status, post_slug: slug } = critique;
  if (status === 'published' && slug) {
    const href = `${SITE}/posts/${slug}/`;
    return `<a class="badge badge-done" href="${href}" target="_blank" rel="noopener">비평</a>`;
  }
  if (status === 'in_progress') return '<span class="badge badge-progress">진행</span>';
  if (status === 'planned') return '<span class="badge badge-progress">예정</span>';
  return '';
}

function renderList() {
  const filtered = getFiltered();
  const list = document.getElementById('list');
  list.innerHTML = '';

  filtered.forEach((item) => {
    const a = item.axes;
    const nav = normNav(a.navigation).map(label).join('·') || '—';
    const li = document.createElement('li');
    li.innerHTML = `
      <div class="row-head">
        <span class="badge badge-id">${escapeHtml(item.inventory_id)}</span>
        <a class="row-title" href="${item.url}" target="_blank" rel="noopener">${escapeHtml(item.title)}</a>
        ${critiqueBadge(item.critique)}
        ${item.has_manual_yaml ? '<span class="badge badge-yaml">YAML</span>' : ''}
      </div>
      <span class="row-meta">
        <span class="tag-pill">${escapeHtml(shortGroup(item.group))}</span>
        ${label(a.operator)} · ${label(a.unit)} · 형식 ${label(a.form_experiment)} · ${nav}
      </span>
    `;
    list.appendChild(li);
  });

  document.getElementById('result-count').textContent = `${filtered.length} / ${data.total}`;
  document.getElementById('empty').hidden = filtered.length > 0;
  renderActiveFilters();
}

function escapeHtml(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function renderMatrix() {
  const ops = ['institution', 'community', 'individual', 'hybrid', 'corporate'];
  const forms = ['high', 'medium', 'low'];
  const grid = {};
  data.items.forEach((item) => {
    const k = `${item.axes.operator}|${item.axes.form_experiment}`;
    grid[k] = (grid[k] || 0) + 1;
  });
  const table = document.getElementById('matrix-table');
  let html = '<tr><th></th>' + forms.map((f) => `<th>${label(f)}</th>`).join('') + '</tr>';
  ops.forEach((op) => {
    html += `<tr><th>${label(op)}</th>`;
    forms.forEach((f) => {
      const n = grid[`${op}|${f}`] || 0;
      const hot = n >= 15 ? ' hot' : '';
      html += `<td class="${n ? '' : 'empty'}${hot}">${n || '·'}</td>`;
    });
    html += '</tr>';
  });
  table.innerHTML = html;
}

function clearAll(rerenderPresets = true) {
  active.clear();
  showCritiqueCandidates = false;
  document.getElementById('search').value = '';
  document.getElementById('only-critique').checked = false;
  document.getElementById('only-yaml').checked = false;
  if (rerenderPresets) {
    document.querySelectorAll('.preset').forEach((p) => p.classList.remove('active'));
  }
  renderFacets();
  renderList();
}

function applyPreset(name) {
  clearAll(false);
  document.querySelectorAll('.preset').forEach((p) => {
    p.classList.toggle('active', p.dataset.preset === name);
  });

  if (name === 'critique') {
    showCritiqueCandidates = true;
  } else if (name === 'all') {
    /* clearAll already ran */
  } else if (name === 'form-high') {
    active.set('form_experiment', new Set(['high']));
  } else if (name === 'korea') {
    active.set('locale', new Set(['KR']));
  }
  renderFacets();
  renderList();
}

async function init() {
  const res = await fetch('data/arena/inventory-enriched.json');
  if (!res.ok) throw new Error(res.statusText);
  data = await res.json();

  document.getElementById('title-count').textContent = data.total;
  document.getElementById('built-at').textContent =
    `데이터 ${data.built_at} · 추론 ${data.total - data.manual_yaml_count} + YAML ${data.manual_yaml_count}`;

  renderStats();
  renderMatrix();
  renderFacets();
  renderList();

  document.getElementById('app').hidden = false;

  document.getElementById('search').addEventListener('input', renderList);
  ['only-critique', 'only-yaml'].forEach((id) => {
    document.getElementById(id).addEventListener('change', () => {
      if (id === 'only-critique') showCritiqueCandidates = false;
      document.querySelectorAll('.preset').forEach((p) => p.classList.remove('active'));
      renderList();
    });
  });
  document.getElementById('sort').addEventListener('change', (e) => {
    sortBy = e.target.value;
    renderList();
  });
  document.getElementById('clear-facets').addEventListener('click', () => clearAll(true));
  document.querySelectorAll('.preset').forEach((btn) => {
    btn.addEventListener('click', () => applyPreset(btn.dataset.preset));
  });
}

init().catch((err) => {
  const box = document.getElementById('load-error');
  box.hidden = false;
  console.error(err);
});
