# Netlify Path Configuration Guide

## Option 1: Configure as Subdirectory on Main Domain (Recommended)

If you want `https://joseprendergast.com/Mistica_original_Web_2005` to serve this site:

### Method A: Using Netlify Redirects (Main Site)

If `joseprendergast.com` is already a Netlify site, add this to your **main site's** `netlify.toml`:

```toml
[[redirects]]
  from = "/Mistica_original_Web_2005/*"
  to = "https://your-mistica-site.netlify.app/:splat"
  status = 200
  force = true
```

Replace `your-mistica-site.netlify.app` with your actual Netlify site URL.

### Method B: Using Netlify Split Testing/Path-based Routing

1. Go to your **main site** on Netlify dashboard
2. Navigate to **Site settings** → **Split testing**
3. Configure path-based routing to proxy `/Mistica_original_Web_2005/*` to your Mistica site

### Method C: Deploy as Subdirectory (Single Site)

If you want everything in one Netlify site:

1. In your main site's repository, create folder: `Mistica_original_Web_2005/`
2. Copy all files from `Mistica New Generation/` to `Mistica_original_Web_2005/`
3. Update `netlify.toml` in main site:

```toml
[[redirects]]
  from = "/Mistica_original_Web_2005/*"
  to = "/Mistica_original_Web_2005/:splat"
  status = 200
```

## Option 2: Separate Netlify Site with Custom Domain Path

If this is a **separate Netlify site**:

1. Go to your Mistica site on Netlify dashboard
2. **Site settings** → **Domain management**
3. Click **Add custom domain**
4. Enter: `joseprendergast.com`
5. After verification, go to **Domain settings**
6. Add **Subdomain** or configure **Path prefix**:
   - For path prefix, you'll need to configure this in your DNS/hosting provider
   - Or use Netlify's proxy redirects from your main site

## Option 3: Netlify Proxy Redirect (Easiest)

In your **main joseprendergast.com site's** `netlify.toml`, add:

```toml
[[redirects]]
  from = "/Mistica_original_Web_2005/*"
  to = "https://mistica-web-2005.netlify.app/:splat"
  status = 200
  force = true
  headers = {X-From = "Netlify"}
```

This will proxy all requests from `/Mistica_original_Web_2005/*` to your Mistica site.

## Recommended Approach

**Use Option 3 (Proxy Redirect)** - It's the simplest:
1. Your Mistica site stays as a separate Netlify site
2. Add the redirect rule to your main `joseprendergast.com` site
3. All paths will work correctly

## Testing

After configuration, test:
- `https://joseprendergast.com/Mistica_original_Web_2005/` → Should show indexReal.htm
- `https://joseprendergast.com/Mistica_original_Web_2005/indexReal.htm` → Should work
- `https://joseprendergast.com/Mistica_original_Web_2005/menu.htm` → Should work
