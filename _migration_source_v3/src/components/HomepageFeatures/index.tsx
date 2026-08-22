import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';
import {useColorMode} from '@docusaurus/theme-common/internal';

type FeatureItem = {
  title: string;
  LightSvg: React.ComponentType<React.ComponentProps<'svg'>>;
  DarkSvg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Block Zero-Hour Threats at the Perimeter',
    LightSvg: require('@site/static/img/free2use_light.svg').default,
    DarkSvg: require('@site/static/img/free2use.svg').default,
    description: (
      <>
        Pre-execution blocking of phishing, malware, ransomware, and data exfiltration hidden in HTTPS traffic. Deploy on-premises, cloud, or hybrid in 15 minutes via the <Link href='https://key.safesquid.com'>SafeSquid Self-Service Portal</Link>.
      </>
    ),
  },
  {
    title: 'Enterprise-Ready Integration',
    LightSvg: require('@site/static/img/integrations_light.svg').default,
    DarkSvg: require('@site/static/img/integrations.svg').default,
    description: (
      <>
        Agent-less integration with IAM systems, ICAP servers, DLP solutions, SIEMs, and SoC threat intelligence. Purpose-built for Zero-Trust architectures.
      </>
    ),
  },
  {
    title: 'Scale Without Performance Degradation',
    LightSvg: require('@site/static/img/scale_light.svg').default,
    DarkSvg: require('@site/static/img/scale.svg').default,
    description: (
      <>
        SMP-aware architecture scales up to absorb load bursts without IPC bottlenecks. Scale out with cluster-ready technology for load balancing and fail-over. No session drops, no logging gaps.
      </>
    ),
  },
];

function Feature({title, LightSvg, DarkSvg, description}: FeatureItem) {
  const {isDarkTheme} = useColorMode();
  const Svg = isDarkTheme ? DarkSvg : LightSvg;
  
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
