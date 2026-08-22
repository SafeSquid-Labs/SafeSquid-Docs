import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';
import * as fs from 'fs';
import * as path from 'path';

// Define the base directory
const BASE_DIR = 'docs';

// Function to recursively process directories
function generateJson(dirPath: string): any[] {
    const mdFiles = fs.readdirSync(dirPath).filter(file => file.endsWith('.md') && file !== 'main.md');
    const mainMdPath = path.join(dirPath, 'main.md');
    const hasMainMd = fs.existsSync(mainMdPath);

    const items: any[] = [];
    fs.readdirSync(dirPath).forEach(entry => {
        const entryPath = path.join(dirPath, entry);
        if (fs.statSync(entryPath).isDirectory()) {
            items.push(...generateJson(entryPath));
        } else if (entry !== 'main.md' && entry.endsWith('.md')) {
            const fileId = entryPath
                .replace(`${BASE_DIR}/`, '')
                .replace(/^[0-9]+-/g, '')
                .replace(/\/[0-9]+-/g, '/')
                .replace(/\.md$/, '');
            items.push({ type: 'doc', id: fileId });
        }
    });

    if (hasMainMd) {
        const cleanMainId = dirPath
            .replace(`${BASE_DIR}/`, '')
            .replace(/^[0-9]+-/g, '')
            .replace(/\/[0-9]+-/g, '/')
            .concat('/main');
        return [
            {
                type: 'category',
                label: path.basename(dirPath).replace(/^[0-9]+-/, '').replace(/_/g, ' '),
                link: { type: 'doc', id: cleanMainId },
                items: items,
            },
        ];
    }

    return items;
}

// Generate the JSON structure starting from the base directory
const sidebarSchema = generateJson(BASE_DIR).flat();

// Remove the top-level "docs" category
const sidebars: SidebarsConfig = {
    tutorialSidebar: sidebarSchema as unknown as SidebarsConfig['tutorialSidebar'],
};

export default sidebars;