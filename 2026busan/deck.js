/**
 * presentation-split — slide loader + navigation
 * Mirrors presentation.html behavior.
 */
(function () {
    const SLIDE_IDS = [
    "s01",
    "s02",
    "s03",
    "s04",
    "s05",
    "s06",
    "s07",
    "s08",
    "s09",
    "s10",
    "s11",
    "s12",
    "s13",
    "s14",
    "s15",
    "s16",
    "s17",
    "s18",
    "s19",
    "s20",
    "s21",
    "s22",
    "s23",
    "s24",
    "s27",
    "s28",
    "s31",
    "s32",
    "s34",
    "s35",
    "s36"
    ];

    const deck = document.getElementById("deck");
    const nav = document.getElementById("nav");
    let slides = [];
    let current = 0;

    async function loadSlides() {
        const fragments = await Promise.all(
            SLIDE_IDS.map(async (id) => {
                const res = await fetch(`slides/${id}.html`);
                if (!res.ok) throw new Error(`Failed to load slides/${id}.html`);
                return res.text();
            }),
        );
        deck.innerHTML = fragments.join("\n");
        slides = Array.from(deck.querySelectorAll(".slide"));
        initNav();
    }

    function goTo(n) {
        if (!slides.length) return;
        slides[current].classList.remove("active");
        current = Math.max(0, Math.min(n, slides.length - 1));
        slides[current].classList.add("active");
        if (current === 0 || current === slides.length - 1) {
            nav.textContent = "";
        } else {
            nav.textContent = current + 1;
        }
        history.replaceState(
            null,
            "",
            "#" + slides[current].id,
        );
    }
    window.goTo = goTo;

    function initNav() {
        document.addEventListener("keydown", function (e) {
            if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
                e.preventDefault();
                goTo(current + 1);
            }
            if (e.key === "ArrowLeft" || e.key === "PageUp") {
                e.preventDefault();
                goTo(current - 1);
            }
            if (e.key === "Home") {
                e.preventDefault();
                goTo(0);
            }
            if (e.key === "End") {
                e.preventDefault();
                goTo(slides.length - 1);
            }
        });

        let tx = 0;
        document.addEventListener(
            "touchstart",
            function (e) {
                tx = e.touches[0].clientX;
            },
            { passive: true },
        );
        document.addEventListener("touchend", function (e) {
            const dx = e.changedTouches[0].clientX - tx;
            if (Math.abs(dx) > 50) goTo(dx < 0 ? current + 1 : current - 1);
        });

        document.addEventListener("click", function (e) {
            if (e.target.closest("a")) return;
            if (e.target.closest(".term")) return;
            if (e.target.closest("details") || e.target.closest("summary")) return;
            goTo(e.clientX < window.innerWidth / 2 ? current - 1 : current + 1);
        });

        const hash = window.location.hash;
        const init = hash ? SLIDE_IDS.indexOf(hash.replace("#", "")) : 0;
        goTo(init >= 0 ? init : 0);
    }

    loadSlides().catch((err) => {
        deck.innerHTML =
            '<p style="padding:2rem;font-family:sans-serif;color:#666;">슬라이드를 불러오지 못했습니다. 로컬 서버에서 열어주세요.<br><code>npx serve .</code> (repo root) → /presentation-split/</p>';
        console.error(err);
    });
})();
