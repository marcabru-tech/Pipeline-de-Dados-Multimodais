import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  srcDir: 'src',
  integrations: [tailwind()],
  output: 'static',
  site: 'https://marcabru-tech.github.io/',
});
