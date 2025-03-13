import type { StorybookConfig } from '@storybook/react-webpack5';

const config: StorybookConfig = {
  stories: [
    "../stories/**/*.mdx",
    "../stories/**/*.stories.@(js|jsx|mjs|ts|tsx)"
  ],
  addons: [
    "@storybook/addon-webpack5-compiler-swc",
    "@storybook/addon-essentials",
    "@storybook/addon-onboarding",
    "@chromatic-com/storybook",
    "@storybook/addon-interactions"
  ],
  framework: {
    name: "@storybook/react-webpack5",
    options: {}
  },
  // webpackFinal을 통해 Webpack 설정을 수정
  webpackFinal: async (config) => {
    // config.module이 없다면 빈 객체로 초기화하고 rules를 빈 배열로 설정
    if (!config.module) {
      config.module = { rules: [] }; // rules는 빈 배열로 초기화
    }

    // config.module.rules가 undefined일 경우를 처리
    if (!config.module.rules) {
      config.module.rules = []; // rules가 없다면 빈 배열로 초기화
    }

    // Babel 로더 설정 추가 (Emotion 사용을 위한 Babel 플러그인 포함)
    config.module.rules.push({
      test: /\.(js|mjs|jsx|ts|tsx)$/,
      use: [
        {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-react',  // React JSX 처리
              '@babel/preset-typescript',  // TypeScript 처리
            ],
            plugins: [
              '@emotion/babel-plugin',  // Emotion 스타일링을 위한 Babel 플러그인
            ],
          },
        },
      ],
    });

    // 수정된 config 반환
    return config;
  },
};

export default config;
