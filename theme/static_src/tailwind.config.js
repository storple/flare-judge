/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
	    */
	    // '../../**/*.py'
        
        // classes included in markdown
	    '../../learn/markdown.py'
    ],
	theme: {
        extend: {
		colors: {
			transparent: 'transparent',
			current: 'currentColor',
			'text': {
				50: 'hsl(var(--text-50))',
				100: 'hsl(var(--text-100))',
				200: 'hsl(var(--text-200))',
				300: 'hsl(var(--text-300))',
				400: 'hsl(var(--text-400))',
				500: 'hsl(var(--text-500))',
				600: 'hsl(var(--text-600))',
				700: 'hsl(var(--text-700))',
				800: 'hsl(var(--text-800))',
				900: 'hsl(var(--text-900))',
				950: 'hsl(var(--text-950))',
				DEFAULT: 'hsl(var(--text-900))',
				light: 'hsl(var(--text-900))',
				dark: 'hsl(var(--text-100))',
			},
			'background': {
				50: 'hsl(var(--background-50))',
				100: 'hsl(var(--background-100))',
				200: 'hsl(var(--background-200))',
				300: 'hsl(var(--background-300))',
				400: 'hsl(var(--background-400))',
				500: 'hsl(var(--background-500))',
				600: 'hsl(var(--background-600))',
				700: 'hsl(var(--background-700))',
				800: 'hsl(var(--background-800))',
				900: 'hsl(var(--background-900))',
				950: 'hsl(var(--background-950))',
				DEFAULT: 'hsl(var(--background-500))',
				light: 'hsl(var(--background-100))',
				dark: 'hsl(var(--background-800))',
			},
			'primary': {
				50: 'hsl(var(--primary-50))',
				100: 'hsl(var(--primary-100))',
				200: 'hsl(var(--primary-200))',
				300: 'hsl(var(--primary-300))',
				400: 'hsl(var(--primary-400))',
				500: 'hsl(var(--primary-500))',
				600: 'hsl(var(--primary-600))',
				700: 'hsl(var(--primary-700))',
				800: 'hsl(var(--primary-800))',
				900: 'hsl(var(--primary-900))',
				950: 'hsl(var(--primary-950))',
				DEFAULT: 'hsl(var(--primary-500))',
				light: 'hsl(var(--primary-100))',
				dark: 'hsl(var(--primary-800))',
			},
			'secondary': {
				50: 'hsl(var(--secondary-50))',
				100: 'hsl(var(--secondary-100))',
				200: 'hsl(var(--secondary-200))',
				300: 'hsl(var(--secondary-300))',
				400: 'hsl(var(--secondary-400))',
				500: 'hsl(var(--secondary-500))',
				600: 'hsl(var(--secondary-600))',
				700: 'hsl(var(--secondary-700))',
				800: 'hsl(var(--secondary-800))',
				900: 'hsl(var(--secondary-900))',
				950: 'hsl(var(--secondary-950))',
				DEFAULT: 'hsl(var(--secondary-500))',
				light: 'hsl(var(--secondary-100))',
				dark: 'hsl(var(--secondary-900))',
			},
			'accent': {
				50: 'hsl(var(--accent-50))',
				100: 'hsl(var(--accent-100))',
				200: 'hsl(var(--accent-200))',
				300: 'hsl(var(--accent-300))',
				400: 'hsl(var(--accent-400))',
				500: 'hsl(var(--accent-500))',
				600: 'hsl(var(--accent-600))',
				700: 'hsl(var(--accent-700))',
				800: 'hsl(var(--accent-800))',
				900: 'hsl(var(--accent-900))',
				950: 'hsl(var(--accent-950))',
				DEFAULT: 'hsl(var(--accent-500))',
				light: 'hsl(var(--accent-100))',
				dark: 'hsl(var(--accent-900))',
			},
		},
	},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
