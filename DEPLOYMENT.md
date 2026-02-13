# Deployment Guide - Mistica Web to Netlify

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `mistica-web-2005` (or your preferred name)
3. Description: "Original Mistica band website from 2005"
4. Choose **Public** or **Private**
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Push to GitHub

Run these commands in your terminal:

```bash
cd "/Users/jose_fernandez/Library/CloudStorage/OneDrive-Personal/Cursor Apps Repo/Mistika Web"

# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mistica-web-2005.git

# Rename branch to main if needed
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Deploy to Netlify

1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Click "GitHub" and authorize Netlify if needed
4. Select your `mistica-web-2005` repository
5. Configure build settings:
   - **Build command:** (leave empty)
   - **Publish directory:** `Mistica New Generation`
6. Click "Deploy site"

## Step 4: Configure Custom Domain Path

To deploy to `https://joseprendergast.com/Mistica_original_Web_2005`:

1. In Netlify dashboard, go to **Site settings** → **Domain management**
2. Click **Add custom domain**
3. Enter: `joseprendergast.com`
4. Follow DNS configuration instructions
5. Once domain is verified, go to **Domain settings** → **Subdomain**
6. Add subdomain/path: `Mistica_original_Web_2005`
7. Or configure as a subdirectory redirect in your main site's `netlify.toml`

Alternatively, if this is a subdirectory of your main site:
- Configure your main Netlify site to proxy this path
- Or use Netlify's path prefix feature

## Step 5: Verify Deployment

After deployment, visit:
- Netlify URL: `https://your-site-name.netlify.app/indexReal.htm`
- Custom domain: `https://joseprendergast.com/Mistica_original_Web_2005/indexReal.htm`

## Troubleshooting

- If images don't load, check that all image paths are relative
- If frames don't work, ensure `_redirects` file is in the publish directory
- Check Netlify build logs for any errors
