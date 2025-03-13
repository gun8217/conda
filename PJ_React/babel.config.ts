import { ConfigAPI } from "@babel/core";

const config = (api: ConfigAPI) => {
  // 캐시를 항상 활성화
  api.cache.forever();

  return {
    presets: [
      "@babel/preset-env",
      "@babel/preset-react",
      "@babel/preset-typescript", // TypeScript 관련 프리셋 추가
    ],
    plugins: [
      "@emotion/babel-plugin", // Emotion 관련 플러그인 추가
    ],
  };
};

export default config;
