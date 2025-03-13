import react from 'eslint-plugin-react';

export default [
  {
    plugins: {
      react, // react 플러그인 객체 사용
    },
    rules: {
      // eslint:recommended의 규칙을 직접 설정 (여기서는 일부 예시만 추가)
      'no-console': 'warn', // 예시: console 사용 시 경고
      'react/jsx-uses-react': 'off', // React 17+에서는 필요없을 수 있음
      'react/react-in-jsx-scope': 'off', // React 17+에서는 필요없을 수 있음
      'react/prop-types': 'off', // PropTypes를 사용하지 않는 경우
      // plugin:react/recommended의 규칙을 직접 설정
      'react/jsx-uses-vars': 'error', // 예시: JSX에서 사용되는 변수가 정의되었는지 체크
      'react/jsx-no-undef': 'error', // 예시: JSX에서 정의되지 않은 변수를 사용하지 않도록
    },
    settings: {
      react: {
        version: '19', // 사용 중인 React 버전
      },
    },
  },
];
