import js from '@eslint/js';
import jupyter from '@jupyter/eslint-plugin';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  {
    ignores: [
      'node_modules/**',
      'lib/**',
      'dist/**',
      'neat_notebook/labextension/**',
      'test-results/**',
      'playwright-report/**',
      '.yarn/**',
      '.venv*/**',
    ],
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  { languageOptions: { globals: { ...globals.browser, ...globals.node } } },
  {
    files: ['**/*.ts'],
    languageOptions: {
      parserOptions: {
        project: './tsconfig.eslint.json',
        tsconfigRootDir: import.meta.dirname,
      },
    },
    plugins: { jupyter },
    rules: {
      '@typescript-eslint/no-namespace': 'off',
      '@typescript-eslint/no-explicit-any': 'off',
      'jupyter/plugin-description': 'error',
      'jupyter/plugin-id-convention': 'error',
      'jupyter/plugin-activation-args': 'error',
      'jupyter/require-signal-cleanup': 'error',
      'jupyter/require-signal-this-arg': 'error',
      'jupyter/no-translation-concatenation': 'error',
      'jupyter/no-dynamic-translation': 'error',
      'jupyter/no-untranslated-string': 'error',
      curly: ['error', 'all'],
      eqeqeq: 'error',
    },
  }
);
