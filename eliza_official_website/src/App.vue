<template>
  <div :class="['bg', { showHome }]">
    <div :style="[bgBallStyle.common, bgBallStyle.top]"></div>
    <div :style="[bgBallStyle.common, bgBallStyle.bottom]"></div>
  </div>
  <div class="text">
    <span style="text-align: center">{{ text }}</span>
    <span v-show="cursorVisible" class="cursor"></span>
  </div>
  <header
    :style="{
      opacity: showHome ? 1 : 0,
      pointerEvents: showHome ? 'auto' : 'none',
    }"
  >
    <spank style="padding-left: 20px; font-size: 13px"
      >eliza community</spank
    >
    <div style="display: flex; gap: 12px; padding-right: 20px">
      <a target="_blank" href="https://x.com/elizacommunity" style="scale: 0.8" alt="https://x.com/elizacommunity">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          version="1.1"
          id="Layer_1"
          width="24px"
          height="24px"
          viewBox="0 0 24 24"
          style="enable-background: new 0 0 24 24"
          xml:space="preserve"
        >
          <path
            fill="#fff"
            d="M14.095479,10.316482L22.286354,1h-1.940718l-7.115352,8.087682L7.551414,1H1l8.589488,12.231093L1,23h1.940717  l7.509372-8.542861L16.448587,23H23L14.095479,10.316482z M11.436522,13.338465l-0.871624-1.218704l-6.924311-9.68815h2.981339  l5.58978,7.82155l0.867949,1.218704l7.26506,10.166271h-2.981339L11.436522,13.338465z"
          />
        </svg>
      </a>
      <a target="_blank" href="https://t.me/elizactocommunity" style="scale: 0.9; translate: -1px 0px" alt="https://t.me/elizactocommunity">
        <!DOCTYPE svg PUBLIC '-//W3C//DTD SVG 1.1//EN' 'http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd'>
        <svg
          height="24px"
          style="enable-background: new 0 0 512 512"
          version="1.1"
          viewBox="0 0 512 512"
          xml:space="preserve"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
        >
          <g id="_x33_35-telegram">
            <g>
              <g>
                <path
                  d="M484.689,98.231l-69.417,327.37c-5.237,23.105-18.895,28.854-38.304,17.972L271.2,365.631     l-51.034,49.086c-5.646,5.647-10.371,10.372-21.256,10.372l7.598-107.722L402.539,140.23c8.523-7.598-1.848-11.809-13.247-4.21     L146.95,288.614L42.619,255.96c-22.694-7.086-23.104-22.695,4.723-33.579L455.423,65.166     C474.316,58.081,490.85,69.375,484.689,98.231z"
                  style="fill: #fff"
                />
              </g>
            </g>
          </g>
          <g id="Layer_1" />
        </svg>
      </a>
      <a target="_blank" href="https://dexscreener.com/solana/2pofQcvn4wysAzpSqPPxQ4cSPBtKQLSEHF9q5x77Avm7" style="width: 24px; height: 24px; scale: 0.85" alt="https://dexscreener.com/solana/2pofQcvn4wysAzpSqPPxQ4cSPBtKQLSEHF9q5x77Avm7">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="100%"
          height="100%"
          fill="#fff"
          fill-rule="evenodd"
          viewBox="0 0 252 300"
          focusable="false"
          class="chakra-icon custom-euf446"
        >
          <path
            d="M151.818 106.866c9.177-4.576 20.854-11.312 32.545-20.541 2.465 5.119 2.735 9.586 1.465 13.193-.9 2.542-2.596 4.753-4.826 6.512-2.415 1.901-5.431 3.285-8.765 4.033-6.326 1.425-13.712.593-20.419-3.197m1.591 46.886l12.148 7.017c-24.804 13.902-31.547 39.716-39.557 64.859-8.009-25.143-14.753-50.957-39.556-64.859l12.148-7.017a5.95 5.95 0 003.84-5.845c-1.113-23.547 5.245-33.96 13.821-40.498 3.076-2.342 6.434-3.518 9.747-3.518s6.671 1.176 9.748 3.518c8.576 6.538 14.934 16.951 13.821 40.498a5.95 5.95 0 003.84 5.845zM126 0c14.042.377 28.119 3.103 40.336 8.406 8.46 3.677 16.354 8.534 23.502 14.342 3.228 2.622 5.886 5.155 8.814 8.071 7.897.273 19.438-8.5 24.796-16.709-9.221 30.23-51.299 65.929-80.43 79.589-.012-.005-.02-.012-.029-.018-5.228-3.992-11.108-5.988-16.989-5.988s-11.76 1.996-16.988 5.988c-.009.005-.017.014-.029.018-29.132-13.66-71.209-49.359-80.43-79.589 5.357 8.209 16.898 16.982 24.795 16.709 2.929-2.915 5.587-5.449 8.814-8.071C69.31 16.94 77.204 12.083 85.664 8.406 97.882 3.103 111.959.377 126 0m-25.818 106.866c-9.176-4.576-20.854-11.312-32.544-20.541-2.465 5.119-2.735 9.586-1.466 13.193.901 2.542 2.597 4.753 4.826 6.512 2.416 1.901 5.432 3.285 8.766 4.033 6.326 1.425 13.711.593 20.418-3.197"
          />
          <path
            d="M197.167 75.016c6.436-6.495 12.107-13.684 16.667-20.099l2.316 4.359c7.456 14.917 11.33 29.774 11.33 46.494l-.016 26.532.14 13.754c.54 33.766 7.846 67.929 24.396 99.193l-34.627-27.922-24.501 39.759-25.74-24.231L126 299.604l-41.132-66.748-25.739 24.231-24.501-39.759L0 245.25c16.55-31.264 23.856-65.427 24.397-99.193l.14-13.754-.016-26.532c0-16.721 3.873-31.578 11.331-46.494l2.315-4.359c4.56 6.415 10.23 13.603 16.667 20.099l-2.01 4.175c-3.905 8.109-5.198 17.176-2.156 25.799 1.961 5.554 5.54 10.317 10.154 13.953 4.48 3.531 9.782 5.911 15.333 7.161 3.616.814 7.3 1.149 10.96 1.035-.854 4.841-1.227 9.862-1.251 14.978L53.2 160.984l25.206 14.129a41.926 41.926 0 015.734 3.869c20.781 18.658 33.275 73.855 41.861 100.816 8.587-26.961 21.08-82.158 41.862-100.816a41.865 41.865 0 015.734-3.869l25.206-14.129-32.665-18.866c-.024-5.116-.397-10.137-1.251-14.978 3.66.114 7.344-.221 10.96-1.035 5.551-1.25 10.854-3.63 15.333-7.161 4.613-3.636 8.193-8.399 10.153-13.953 3.043-8.623 1.749-17.689-2.155-25.799l-2.01-4.175z"
          />
        </svg>
      </a>
    </div>
  </header>
  <div class="main" :style="{ pointerEvents: showHome ? 'auto' : 'none' }">
    <!-- <img src="/eliza.gif" alt=""> -->
    <div
      class="media"
      :style="{
        opacity: showHome ? 1 : 0,
        translate: showHome ? '0 0' : '-30% 0',
      }"
    >
      <!-- <img src="/eliza2.png" alt="eliza" /> -->
       <video src="/eliza.mp4" autoplay="true" loop muted></video>
    </div>

    <section :style="['font-size: 14px;line-height: 2', { opacity: showHome ? 1 : 0 }]">
      <p style="color: orange">contract-address(CA):</p>
      <p style="color: orange">wUtwjNmjCP9TTTtoc5Xn5h5sZ2cYJm5w2w44b79yr2o</p>
      <p>
        The Battle of Uppercase vs Lowercase: Community vs. Conspiracy Group
      </p>
      <p>
        The $eliza project has turned into a full-blown war between $eliza
        (lowercase) and $ELIZA (uppercase)—and it’s not just about token
        symbols. This is about decentralization vs. capital control, with the
        community stuck in the middle, fighting for its future.
      </p>
      <p>$eliza – The Power of the Community</p>
      <p>
        At first, $eliza was all about decentralization. $eliza (lowercase)
        represented the community—everyday investors, developers, and anyone who
        believed in the power of the people over centralized control. This token
        was built on the idea that the community should drive the project, and
        that community strength was what would push $eliza forward.
      </p>
      <p>$ELIZA – The Conspiracy Group Takes Over</p>
      <p>
        But things started to shift. Shaw sold off all his $eliza (lowercase)
        and at the same time, launched $ELIZA with the backing of a conspiracy
        group. They started buying up $ELIZA through pump-and-dump schemes (aka
        "rat trading"), manipulating the market, and completely ignoring the
        community’s interests. This wasn’t a project for the people anymore—it
        was hijacked by big capital, controlled by a handful of wealthy players.
      </p>
      <p>
        What was their goal? To centralize control, pump the token for profit,
        and shut the community out of the decision-making process. $ELIZA became
        just another tool for market manipulation, leaving $eliza and the
        principles of decentralization in the dust.
      </p>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

const text = ref("");

const cursorVisible = ref(false);

const showHome = ref(false);

const size =
  (window.innerWidth > window.innerHeight
    ? window.innerWidth
    : window.innerHeight) * 0.75;

const bgBallStyle = ref({
  common: {
    opacity: 0.1,
    scale: 1,
    width: `${size}px`,
    height: `${size}px`,
  },
  top: {
    translate: "0 -65%",
  },
  bottom: {
    translate: "0 65%",
  },
});

onMounted(() => {
  setTimeout(() => {
    bgBallStyle.value.common.opacity = 0.8;
    bgBallStyle.value.top.translate = `0 -55%`;
    bgBallStyle.value.bottom.translate = `0 55%`;
  }, 100);

  setTimeout(() => {
    cursorVisible.value = true;
    animation();
  }, 1000);
});

function animation() {
  const fullText = [
    "Hi, i'm eliza",
    "Welcome to our community",
    "Join us, to build our dream",
  ];

  function inputText() {
    const id = setInterval(() => {
      text.value += fullText[0].charAt(text.value.length);

      if (text.value.length === fullText[0].length) {
        clearInterval(id);
        setTimeout(clearText, 1000);
      }
    }, 100);
  }

  function clearText() {
    const id = setInterval(() => {
      text.value = text.value.slice(0, -1);

      if (text.value === "") {
        clearInterval(id);

        fullText.shift();

        if (fullText.length > 0) {
          inputText();
        } else {
          cursorVisible.value = false;
          showHome.value = true;
          bgBallStyle.value.common.scale = 1.2;
          bgBallStyle.value.common.opacity = 0;
          bgBallStyle.value.top.translate = `-100% -70%`;
          bgBallStyle.value.bottom.translate = `100% 70%`;
        }
      }
    }, 30);
  }

  inputText();
}
</script>

<style scoped>
.bg {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg > div:nth-child(1) {
  border-radius: 100%;
  box-shadow: inset 0 0 4em 3em rgba(238, 200, 175, 0.2),
    inset 0 0 2em 0.4em rgba(238, 200, 175, 0.2),
    0 0 0.1em 0.1em rgba(238, 200, 175, 0.2),
    0 0 1em 0.4em rgba(238, 200, 175, 0.3);
}

.bg > div:nth-child(2) {
  border-radius: 100%;
  box-shadow: inset 0 0 4em 3em rgba(238, 200, 175, 0.2),
    inset 0 0 2em 0.4em rgba(238, 200, 175, 0.2),
    0 0 0.1em 0.1em rgba(238, 200, 175, 0.2),
    0 0 1em 0.4em rgba(238, 200, 175, 0.3);
}

.bg > div {
  position: absolute;
  transition: all 1.2s ease-in-out;
}

.text {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.text > .cursor {
  border-right: 2px solid rgba(255, 255, 255, 0.8);
  height: 20px;
  animation: cursor 0.6s infinite steps(1, start);
}

@keyframes cursor {
  0% {
    opacity: 0;
  }

  50% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  transition: opacity 0.5s ease-in-out;
}

.main {
  position: absolute;
  top: 52px;
  left: 0;
  display: flex;
  justify-content: space-between;
  align-items: start;
  width: 100%;
}

@media screen and (max-width: 768px) {
  .main {
    display: block;
  }
}

@media screen and (min-width: 769px){
  video {
    max-width: 50vw;
  }
}

.main > .media {
  padding: 0 20px;
  transition: all 1s ease-in-out 1s;
}

.main > .media > img {
  width: 100%;
  object-fit: cover;
}

.main > .media > video {
  width: 100%;
  height: calc(100vh - 52px);
  border-radius: 24px;
  object-fit: cover;
  filter: saturate(0.9);
}

section {
  flex: 1;
  padding: 0 20px;
  text-align: center;
  transition: all 1s ease-in-out 1s;
  overflow-y: scroll;
  height: calc(100vh - 52px);
}
</style>
