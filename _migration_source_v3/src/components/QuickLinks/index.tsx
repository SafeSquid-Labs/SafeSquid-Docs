import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type QuickLinkItem = {
  title: string;
  link: string;
  icon: string;
  description: string;
  priority?: 'primary' | 'secondary';
};

const QuickLinksList: QuickLinkItem[] = [
  {
    title: 'Quick Start (15 min)',
    link: '/docs/Getting_Started/',
    icon: '🚀',
    description: 'Deploy SafeSquid on-premises, cloud, or hybrid. Zero-hour threat defense in 15 minutes.',
    priority: 'primary',
  },
  {
    title: 'SSL Inspection',
    link: '/docs/SSL_Inspection/Configure_HTTPS_Inspection/',
    icon: '🔒',
    description: 'Eliminate the HTTPS blind spot. Inspect encrypted traffic for hidden threats.',
    priority: 'primary',
  },
  {
    title: 'Data Leakage Prevention',
    link: '/docs/Data_Leakage_Prevention/main/',
    icon: '🛡️',
    description: 'Block sensitive data exfiltration at the perimeter. Audit-defensible egress controls.',
    priority: 'primary',
  },
  {
    title: 'Troubleshooting',
    link: '/docs/Troubleshooting/main/',
    icon: '🔧',
    description: 'Diagnose and resolve common SafeSquid configuration issues',
    priority: 'primary',
  },
  {
    title: 'Access Restriction',
    link: '/docs/Access_Restriction/main/',
    icon: '🚦',
    description: 'Enforce acceptable use policies. Granular web access controls by user, group, or time.',
    priority: 'secondary',
  },
  {
    title: 'Authentication',
    link: '/docs/Authentication/main/',
    icon: '👤',
    description: 'Integrate with Active Directory, OpenLDAP, or local credentials for identity-aware security.',
    priority: 'secondary',
  },
  {
    title: 'Reporting & Audit',
    link: '/docs/Audit_Forensics/main/',
    icon: '📊',
    description: 'Immutable audit logs. Board-ready metrics. MTTD/MTTR acceleration for SOC teams.',
    priority: 'secondary',
  },
  {
    title: 'Use Cases',
    link: '/docs/Use_Cases/main/',
    icon: '💡',
    description: 'Real-world configurations for critical infrastructure, banking, regulated enterprises.',
    priority: 'secondary',
  },
];

function QuickLink({title, link, icon, description, priority}: QuickLinkItem) {
  return (
    <div className={clsx('col col--3', styles.quickLinkCard)}>
      <Link to={link} className={clsx(styles.quickLink, priority === 'primary' && styles.primaryLink)}>
        <div className={styles.quickLinkIcon}>{icon}</div>
        <Heading as="h3" className={styles.quickLinkTitle}>{title}</Heading>
        <p className={styles.quickLinkDescription}>{description}</p>
      </Link>
    </div>
  );
}

export default function QuickLinks(): ReactNode {
  return (
    <section className={styles.quickLinksSection}>
      <div className="container">
        <div className="text--center margin-bottom--xl">
          <Heading as="h2">Quick Access to Common Tasks</Heading>
          <p>Jump directly to frequently accessed documentation sections</p>
        </div>
        <div className="row">
          {QuickLinksList.map((props, idx) => (
            <QuickLink key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
