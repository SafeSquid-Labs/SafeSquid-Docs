import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'SafeSquid SWG Documentation',
  tagline: 'Deploy Zero-Trust Web Security in 15 Minutes',
  favicon: 'img/favicon.ico',
  url: 'http://docs.safesquid.com',
  baseUrl: '/',
  trailingSlash: true,
  organizationName: 'SafeSquid-Github',
  projectName: 'docs',
  onBrokenLinks: 'warn',
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          breadcrumbs: true,
          showLastUpdateTime: false,
          showLastUpdateAuthor: false,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
        gtag: {
          trackingID: 'G-ZVZHSKFGQF',
          anonymizeIP: true,
        },
      } as Preset.Options,
    ],
  ],
  plugins: [
    'docusaurus-plugin-image-zoom',
    [
      'docusaurus-pushfeedback', {
        project: 'y2k6wr8viz',
        buttonStyle: 'dark',
      }
    ],
  ],
  themeConfig: {
    image: '@site/static/img/favicon.ico',
    zoom: {
      selector: '.markdown :not(em) > img',
      background: {
        light: 'rgb(255, 255, 255)',
        dark: 'rgb(50, 50, 50)'
      },
      config: {
        // options you can specify via https://github.com/francoischalifour/medium-zoom#usage
      }
    },
    navbar: {
      // title: 'SafeSquid SWG',
      logo: {
        alt: 'SafeSquid Logo',
        src: 'img/SafeSquidBlue.png',   // for light mode
        srcDark: 'img/safesquidWhite.png', // for dark mode
        className: 'safesquid-navbar-logo',
        href: 'https://www.safesquid.com/#home',
      },
      items: [
        {
          href: 'https://www.safesquid.com/#home',
          label: 'HOME',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/#about',
          label: 'ABOUT',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/#features',
          label: 'FEATURES',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/#technology',
          label: 'TECHNOLOGY',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/#solutions',
          label: 'SOLUTIONS',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/#get_started',
          label: 'GET STARTED',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/contact/',
          label: 'CONTACT',
          position: 'left',
        },
        {
          href: 'https://www.safesquid.com/pricing/',
          label: 'PRICING',
          position: 'left',
        },
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'DOCS',
        },
        { 
          to: '/blog', 
          label: 'BLOG', 
          position: 'left' 
        },
        {
          href: 'https://help.safesquid.com/portal/en/community/safesquid-labs',
          label: 'FORUM',
          position: 'left',
        },
        {
          type: 'search',
          position: 'right',
        },
      ],
    },
    docs: {
      sidebar: {
        autoCollapseCategories: true,
        hideable: true,
      },
    },
    tableOfContents: {
      minHeadingLevel: 2,
      maxHeadingLevel: 4,
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} Developed and maintained by SafeSquid Labs, a strategic business unit of Office Efficiencies (INDIA) Private Limited.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash'],
    },
    algolia: {
      appId: 'VDAYH8QLO8',
      apiKey: 'd60fc30e42711815476a72c8b3469240',
      indexName: 'safesquid',
      contextualSearch: true,
      searchPagePath: 'search',
      insights: true,
      searchParameters: {
        facetFilters: [],
        hitsPerPage: 10,
        attributesToSnippet: ['content:50'],
        snippetEllipsisText: '...',
      },
      placeholder: 'Search documentation...',
    },
  } as Preset.ThemeConfig,
};

export default config;
