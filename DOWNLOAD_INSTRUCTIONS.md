# Download & Setup Instructions for Mac

## 🍎 Setup Your Portfolio on Mac

### Step 1: Create React App
```bash
# On your Mac terminal
mkdir ~/sudhanshu-portfolio
cd ~/sudhanshu-portfolio
npx create-react-app . --template cra-template
cd ~/sudhanshu-portfolio
```

### Step 2: Install Additional Dependencies
```bash
npm install @hookform/resolvers@^5.0.1 \
@radix-ui/react-accordion@^1.2.8 \
@radix-ui/react-alert-dialog@^1.1.11 \
@radix-ui/react-aspect-ratio@^1.1.4 \
@radix-ui/react-avatar@^1.1.7 \
@radix-ui/react-checkbox@^1.2.3 \
@radix-ui/react-collapsible@^1.1.8 \
@radix-ui/react-context-menu@^2.2.12 \
@radix-ui/react-dialog@^1.1.11 \
@radix-ui/react-dropdown-menu@^2.1.12 \
@radix-ui/react-hover-card@^1.1.11 \
@radix-ui/react-label@^2.1.4 \
@radix-ui/react-menubar@^1.1.12 \
@radix-ui/react-navigation-menu@^1.2.10 \
@radix-ui/react-popover@^1.1.11 \
@radix-ui/react-progress@^1.1.4 \
@radix-ui/react-radio-group@^1.3.4 \
@radix-ui/react-scroll-area@^1.2.6 \
@radix-ui/react-select@^2.2.2 \
@radix-ui/react-separator@^1.1.4 \
@radix-ui/react-slider@^1.3.2 \
@radix-ui/react-slot@^1.2.0 \
@radix-ui/react-switch@^1.2.2 \
@radix-ui/react-tabs@^1.1.9 \
@radix-ui/react-toast@^1.2.11 \
@radix-ui/react-toggle@^1.1.6 \
@radix-ui/react-toggle-group@^1.1.7 \
@radix-ui/react-tooltip@^1.2.4 \
axios@^1.8.4 \
class-variance-authority@^0.7.1 \
clsx@^2.1.1 \
cmdk@^1.1.1 \
date-fns@^4.1.0 \
embla-carousel-react@^8.6.0 \
input-otp@^1.4.2 \
lucide-react@^0.507.0 \
next-themes@^0.4.6 \
react-day-picker@8.10.1 \
react-hook-form@^7.56.2 \
react-resizable-panels@^3.0.1 \
react-router-dom@^7.5.1 \
sonner@^2.0.3 \
tailwind-merge@^3.2.0 \
tailwindcss-animate@^1.0.7 \
vaul@^1.1.2 \
zod@^3.24.4
```

### Step 3: Install Dev Dependencies
```bash
npm install --save-dev @craco/craco@^7.1.0 \
autoprefixer@^10.4.20 \
postcss@^8.4.49 \
tailwindcss@^3.4.17
```

### Step 4: Download Your Portfolio Files
I'll provide you with all the necessary files to copy into your project.

## 📁 Key Files to Replace/Create:

1. `src/App.js` - Main app component
2. `src/components/` - All portfolio components  
3. `src/data/portfolio.js` - Your portfolio data
4. `public/index.html` - HTML with Google Fonts
5. `tailwind.config.js` - Tailwind configuration
6. `vercel.json` - Deployment configuration

## 🚀 After Setup:

```bash
# Test locally
npm start

# Build for production
npm run build

# Deploy to Vercel
npm install -g vercel
vercel --prod
```

## 📂 File Structure You'll Need:
```
sudhanshu-portfolio/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ui/ (Shadcn components)
│   │   ├── Header.jsx
│   │   ├── Hero.jsx
│   │   ├── About.jsx
│   │   ├── Skills.jsx
│   │   ├── Experience.jsx
│   │   ├── Projects.jsx
│   │   ├── Contact.jsx
│   │   └── Footer.jsx
│   ├── data/
│   │   └── portfolio.js
│   ├── hooks/
│   │   └── use-toast.js
│   ├── App.js
│   ├── index.js
│   └── index.css
├── tailwind.config.js
├── vercel.json
└── package.json
```

Would you like me to provide each file's content for you to copy?