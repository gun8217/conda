import type { StorybookConfig } from '@storybook/react-webpack5';
import path from 'path'; // path 모듈을 임포트

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
  webpackFinal: async (config) => {
    // config.module이 없다면 빈 객체로 초기화
    if (!config.module) {
      config.module = { rules: [] };
    }

    // config.module.rules가 없다면 빈 배열로 초기화
    if (!config.module.rules) {
      config.module.rules = [];
    }

    // Babel 로더 설정 추가 (Emotion 사용을 위한 Babel 플러그인 포함)
    config.module.rules.push({
      test: /\.(js|mjs|jsx|ts|tsx)$/i,
      use: [
        {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-react', // React JSX 처리
              '@babel/preset-typescript', // TypeScript 처리
            ],
            plugins: [
              '@emotion/babel-plugin', // Emotion 스타일링을 위한 Babel 플러그인
            ],
          },
        },
      ],
    });

    // Webpack alias 설정 수정
    config.resolve = {
      ...(config.resolve || {}), // 기존 resolve 설정이 있으면 그대로 사용
      alias: {
        ...(config.resolve?.alias || {}),
        '@': path.resolve(__dirname, '../'), // @를 프로젝트 루트로 설정
      },
    };

    return config;
  },
};

export default config;
