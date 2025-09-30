// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-sobre-mí",
    title: "Sobre mí",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publicaciones",
          title: "Publicaciones",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-traducciónes-y-correcciónes",
          title: "Traducciónes y correcciónes",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/traducciones_y_correcciones/";
          },
        },{id: "dropdown-formación",
              title: "Formación",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/formacion/";
              },
            },{id: "dropdown-docencia",
              title: "Docencia",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/docencia/";
              },
            },{id: "dropdown-investigación",
              title: "Investigación",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/investigacion/";
              },
            },{id: "dropdown-eventos-académicos",
              title: "Eventos académicos",
              description: "",
              section: "Dropdown",
              handler: () => {
                window.location.href = "/eventos_academicos/";
              },
            },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%6D%61%74%69%61%73%67%72%61%66%66%69%67%6E%61@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-instagram',
        title: 'Instagram',
        section: 'Socials',
        handler: () => {
          window.open("https://instagram.com/matigraffi", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/matigraffi", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=uuMqJgAAAAJ", "_blank");
        },
      },{
        id: 'social-custom_social',
        title: 'Custom_social',
        section: 'Socials',
        handler: () => {
          window.open("https://www.goodreads.com/matigraffi", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
