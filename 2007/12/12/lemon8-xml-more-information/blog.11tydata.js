module.exports = {
  tags: "post",
  isPost: true,
  permalink: ({ Slug, slug, Date, Title, title, date, inputPath }) => {
    Date = Date || date;
    Slug = Slug || slug;
    if (!Slug) {
      t = Title || title;
      Slug = t.replace(/ /g, "-").replace(/[^\w-]/g, "").toLowerCase()
    }
    dir = `${Date.toISOString().split("T")[0].replace(/-/g, "/")}/${Slug}/`;
    return `${dir}/index.html`;
  },
  eleventyComputed: {
    date: (data) => {
      d = data.Date || data.date;
      data.page.date = d;
      return d;
    },
    iso_date: (data) => {
      d = data.Date || data.date;
      return d.toISOString().split("T")[0];
    },
   
    title: (data) =>  data.Title || data.title,


  },
};
