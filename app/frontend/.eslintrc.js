module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/vue3-essential',
    '@vue/airbnb',
  ],
  parserOptions: {
    parser: '@babel/eslint-parser',
  },
  rules: {
    "eqeqeq": "off",
    "no-console": "off",
    "no-multiple-empty-lines": ["error", { "max": 2, "maxEOF": 1 }],
    'max-len': ["error", { "code": 150 }],
    'vue/multi-word-component-names': 'off',
    'indent': 'off',
    "eol-last": 0,
    "linebreak-style": 0,
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
  overrides: [
    {
      files: [

        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)',
      ],
      env: {
        jest: true,
      },
    },
  ],
};
