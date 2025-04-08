<!-- # Asala
```
Asala
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  ├─ 0003_customuser_specialization.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers
│  │  ├─ __init__.py
│  │  └─ user.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ build.sh
├─ category
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ clubs
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ communities
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ default.jpeg
├─ generate_fake_data.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ project
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ recommendations
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ urls.py
├─ requirements.txt
├─ search
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ urls.py
└─ staticfiles
   ├─ admin
   │  ├─ css
   │  │  ├─ autocomplete.css
   │  │  ├─ base.css
   │  │  ├─ changelists.css
   │  │  ├─ dark_mode.css
   │  │  ├─ dashboard.css
   │  │  ├─ forms.css
   │  │  ├─ login.css
   │  │  ├─ nav_sidebar.css
   │  │  ├─ responsive.css
   │  │  ├─ responsive_rtl.css
   │  │  ├─ rtl.css
   │  │  ├─ unusable_password_field.css
   │  │  ├─ vendor
   │  │  │  └─ select2
   │  │  │     ├─ LICENSE-SELECT2.md
   │  │  │     ├─ select2.css
   │  │  │     └─ select2.min.css
   │  │  └─ widgets.css
   │  ├─ img
   │  │  ├─ LICENSE
   │  │  ├─ README.txt
   │  │  ├─ calendar-icons.svg
   │  │  ├─ gis
   │  │  │  ├─ move_vertex_off.svg
   │  │  │  └─ move_vertex_on.svg
   │  │  ├─ icon-addlink.svg
   │  │  ├─ icon-alert.svg
   │  │  ├─ icon-calendar.svg
   │  │  ├─ icon-changelink.svg
   │  │  ├─ icon-clock.svg
   │  │  ├─ icon-deletelink.svg
   │  │  ├─ icon-hidelink.svg
   │  │  ├─ icon-no.svg
   │  │  ├─ icon-unknown-alt.svg
   │  │  ├─ icon-unknown.svg
   │  │  ├─ icon-viewlink.svg
   │  │  ├─ icon-yes.svg
   │  │  ├─ inline-delete.svg
   │  │  ├─ search.svg
   │  │  ├─ selector-icons.svg
   │  │  ├─ sorting-icons.svg
   │  │  ├─ tooltag-add.svg
   │  │  └─ tooltag-arrowright.svg
   │  └─ js
   │     ├─ SelectBox.js
   │     ├─ SelectFilter2.js
   │     ├─ actions.js
   │     ├─ admin
   │     │  ├─ DateTimeShortcuts.js
   │     │  └─ RelatedObjectLookups.js
   │     ├─ autocomplete.js
   │     ├─ calendar.js
   │     ├─ cancel.js
   │     ├─ change_form.js
   │     ├─ core.js
   │     ├─ filters.js
   │     ├─ inlines.js
   │     ├─ jquery.init.js
   │     ├─ nav_sidebar.js
   │     ├─ popup_response.js
   │     ├─ prepopulate.js
   │     ├─ prepopulate_init.js
   │     ├─ theme.js
   │     ├─ unusable_password_field.js
   │     ├─ urlify.js
   │     └─ vendor
   │        ├─ jquery
   │        │  ├─ LICENSE.txt
   │        │  ├─ jquery.js
   │        │  └─ jquery.min.js
   │        ├─ select2
   │        │  ├─ LICENSE.md
   │        │  ├─ i18n
   │        │  │  ├─ af.js
   │        │  │  ├─ ar.js
   │        │  │  ├─ az.js
   │        │  │  ├─ bg.js
   │        │  │  ├─ bn.js
   │        │  │  ├─ bs.js
   │        │  │  ├─ ca.js
   │        │  │  ├─ cs.js
   │        │  │  ├─ da.js
   │        │  │  ├─ de.js
   │        │  │  ├─ dsb.js
   │        │  │  ├─ el.js
   │        │  │  ├─ en.js
   │        │  │  ├─ es.js
   │        │  │  ├─ et.js
   │        │  │  ├─ eu.js
   │        │  │  ├─ fa.js
   │        │  │  ├─ fi.js
   │        │  │  ├─ fr.js
   │        │  │  ├─ gl.js
   │        │  │  ├─ he.js
   │        │  │  ├─ hi.js
   │        │  │  ├─ hr.js
   │        │  │  ├─ hsb.js
   │        │  │  ├─ hu.js
   │        │  │  ├─ hy.js
   │        │  │  ├─ id.js
   │        │  │  ├─ is.js
   │        │  │  ├─ it.js
   │        │  │  ├─ ja.js
   │        │  │  ├─ ka.js
   │        │  │  ├─ km.js
   │        │  │  ├─ ko.js
   │        │  │  ├─ lt.js
   │        │  │  ├─ lv.js
   │        │  │  ├─ mk.js
   │        │  │  ├─ ms.js
   │        │  │  ├─ nb.js
   │        │  │  ├─ ne.js
   │        │  │  ├─ nl.js
   │        │  │  ├─ pl.js
   │        │  │  ├─ ps.js
   │        │  │  ├─ pt-BR.js
   │        │  │  ├─ pt.js
   │        │  │  ├─ ro.js
   │        │  │  ├─ ru.js
   │        │  │  ├─ sk.js
   │        │  │  ├─ sl.js
   │        │  │  ├─ sq.js
   │        │  │  ├─ sr-Cyrl.js
   │        │  │  ├─ sr.js
   │        │  │  ├─ sv.js
   │        │  │  ├─ th.js
   │        │  │  ├─ tk.js
   │        │  │  ├─ tr.js
   │        │  │  ├─ uk.js
   │        │  │  ├─ vi.js
   │        │  │  ├─ zh-CN.js
   │        │  │  └─ zh-TW.js
   │        │  ├─ select2.full.js
   │        │  └─ select2.full.min.js
   │        └─ xregexp
   │           ├─ LICENSE.txt
   │           ├─ xregexp.js
   │           └─ xregexp.min.js
   ├─ drf-yasg
   │  ├─ README
   │  ├─ immutable.js
   │  ├─ immutable.min.js
   │  ├─ insQ.js
   │  ├─ insQ.min.js
   │  ├─ redoc
   │  │  ├─ LICENSE
   │  │  ├─ redoc-logo.png
   │  │  ├─ redoc.min.js
   │  │  └─ redoc.standalone.js.map
   │  ├─ redoc-init.js
   │  ├─ redoc-old
   │  │  ├─ LICENSE
   │  │  ├─ redoc.min.js
   │  │  └─ redoc.min.js.map
   │  ├─ style.css
   │  └─ swagger-ui-init.js
   └─ rest_framework
      ├─ css
      │  ├─ bootstrap-theme.min.css
      │  ├─ bootstrap-theme.min.css.map
      │  ├─ bootstrap-tweaks.css
      │  ├─ bootstrap.min.css
      │  ├─ bootstrap.min.css.map
      │  ├─ default.css
      │  ├─ font-awesome-4.0.3.css
      │  └─ prettify.css
      ├─ docs
      │  ├─ css
      │  │  ├─ base.css
      │  │  ├─ highlight.css
      │  │  └─ jquery.json-view.min.css
      │  ├─ img
      │  │  ├─ favicon.ico
      │  │  └─ grid.png
      │  └─ js
      │     ├─ api.js
      │     ├─ highlight.pack.js
      │     └─ jquery.json-view.min.js
      ├─ fonts
      │  ├─ fontawesome-webfont.eot
      │  ├─ fontawesome-webfont.svg
      │  ├─ fontawesome-webfont.ttf
      │  ├─ fontawesome-webfont.woff
      │  ├─ glyphicons-halflings-regular.eot
      │  ├─ glyphicons-halflings-regular.svg
      │  ├─ glyphicons-halflings-regular.ttf
      │  ├─ glyphicons-halflings-regular.woff
      │  └─ glyphicons-halflings-regular.woff2
      ├─ img
      │  ├─ glyphicons-halflings-white.png
      │  ├─ glyphicons-halflings.png
      │  └─ grid.png
      └─ js
         ├─ ajax-form.js
         ├─ bootstrap.min.js
         ├─ coreapi-0.1.1.js
         ├─ csrf.js
         ├─ default.js
         ├─ jquery-3.7.1.min.js
         ├─ load-ajax-form.js
         └─ prettify-min.js

```
```
Asala
├─ README.md
├─ accounts
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ permissions.py
│  ├─ serializers
│  │  ├─ __init__.py
│  │  └─ user.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ asalaDoc.json
├─ build.sh
├─ category
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ clubs
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ communities
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ default.jpeg
├─ generate_fake_data.py
├─ manage.py
├─ products
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  └─ urls.py
├─ project
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ recommendations
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ urls.py
├─ requirements.txt
├─ search
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ api.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ urls.py
└─ staticfiles
   ├─ admin
   │  ├─ css
   │  │  ├─ autocomplete.css
   │  │  ├─ base.css
   │  │  ├─ changelists.css
   │  │  ├─ dark_mode.css
   │  │  ├─ dashboard.css
   │  │  ├─ forms.css
   │  │  ├─ login.css
   │  │  ├─ nav_sidebar.css
   │  │  ├─ responsive.css
   │  │  ├─ responsive_rtl.css
   │  │  ├─ rtl.css
   │  │  ├─ unusable_password_field.css
   │  │  ├─ vendor
   │  │  │  └─ select2
   │  │  │     ├─ LICENSE-SELECT2.md
   │  │  │     ├─ select2.css
   │  │  │     └─ select2.min.css
   │  │  └─ widgets.css
   │  ├─ img
   │  │  ├─ LICENSE
   │  │  ├─ README.txt
   │  │  ├─ calendar-icons.svg
   │  │  ├─ gis
   │  │  │  ├─ move_vertex_off.svg
   │  │  │  └─ move_vertex_on.svg
   │  │  ├─ icon-addlink.svg
   │  │  ├─ icon-alert.svg
   │  │  ├─ icon-calendar.svg
   │  │  ├─ icon-changelink.svg
   │  │  ├─ icon-clock.svg
   │  │  ├─ icon-deletelink.svg
   │  │  ├─ icon-hidelink.svg
   │  │  ├─ icon-no.svg
   │  │  ├─ icon-unknown-alt.svg
   │  │  ├─ icon-unknown.svg
   │  │  ├─ icon-viewlink.svg
   │  │  ├─ icon-yes.svg
   │  │  ├─ inline-delete.svg
   │  │  ├─ search.svg
   │  │  ├─ selector-icons.svg
   │  │  ├─ sorting-icons.svg
   │  │  ├─ tooltag-add.svg
   │  │  └─ tooltag-arrowright.svg
   │  └─ js
   │     ├─ SelectBox.js
   │     ├─ SelectFilter2.js
   │     ├─ actions.js
   │     ├─ admin
   │     │  ├─ DateTimeShortcuts.js
   │     │  └─ RelatedObjectLookups.js
   │     ├─ autocomplete.js
   │     ├─ calendar.js
   │     ├─ cancel.js
   │     ├─ change_form.js
   │     ├─ core.js
   │     ├─ filters.js
   │     ├─ inlines.js
   │     ├─ jquery.init.js
   │     ├─ nav_sidebar.js
   │     ├─ popup_response.js
   │     ├─ prepopulate.js
   │     ├─ prepopulate_init.js
   │     ├─ theme.js
   │     ├─ unusable_password_field.js
   │     ├─ urlify.js
   │     └─ vendor
   │        ├─ jquery
   │        │  ├─ LICENSE.txt
   │        │  ├─ jquery.js
   │        │  └─ jquery.min.js
   │        ├─ select2
   │        │  ├─ LICENSE.md
   │        │  ├─ i18n
   │        │  │  ├─ af.js
   │        │  │  ├─ ar.js
   │        │  │  ├─ az.js
   │        │  │  ├─ bg.js
   │        │  │  ├─ bn.js
   │        │  │  ├─ bs.js
   │        │  │  ├─ ca.js
   │        │  │  ├─ cs.js
   │        │  │  ├─ da.js
   │        │  │  ├─ de.js
   │        │  │  ├─ dsb.js
   │        │  │  ├─ el.js
   │        │  │  ├─ en.js
   │        │  │  ├─ es.js
   │        │  │  ├─ et.js
   │        │  │  ├─ eu.js
   │        │  │  ├─ fa.js
   │        │  │  ├─ fi.js
   │        │  │  ├─ fr.js
   │        │  │  ├─ gl.js
   │        │  │  ├─ he.js
   │        │  │  ├─ hi.js
   │        │  │  ├─ hr.js
   │        │  │  ├─ hsb.js
   │        │  │  ├─ hu.js
   │        │  │  ├─ hy.js
   │        │  │  ├─ id.js
   │        │  │  ├─ is.js
   │        │  │  ├─ it.js
   │        │  │  ├─ ja.js
   │        │  │  ├─ ka.js
   │        │  │  ├─ km.js
   │        │  │  ├─ ko.js
   │        │  │  ├─ lt.js
   │        │  │  ├─ lv.js
   │        │  │  ├─ mk.js
   │        │  │  ├─ ms.js
   │        │  │  ├─ nb.js
   │        │  │  ├─ ne.js
   │        │  │  ├─ nl.js
   │        │  │  ├─ pl.js
   │        │  │  ├─ ps.js
   │        │  │  ├─ pt-BR.js
   │        │  │  ├─ pt.js
   │        │  │  ├─ ro.js
   │        │  │  ├─ ru.js
   │        │  │  ├─ sk.js
   │        │  │  ├─ sl.js
   │        │  │  ├─ sq.js
   │        │  │  ├─ sr-Cyrl.js
   │        │  │  ├─ sr.js
   │        │  │  ├─ sv.js
   │        │  │  ├─ th.js
   │        │  │  ├─ tk.js
   │        │  │  ├─ tr.js
   │        │  │  ├─ uk.js
   │        │  │  ├─ vi.js
   │        │  │  ├─ zh-CN.js
   │        │  │  └─ zh-TW.js
   │        │  ├─ select2.full.js
   │        │  └─ select2.full.min.js
   │        └─ xregexp
   │           ├─ LICENSE.txt
   │           ├─ xregexp.js
   │           └─ xregexp.min.js
   ├─ drf-yasg
   │  ├─ README
   │  ├─ immutable.js
   │  ├─ immutable.min.js
   │  ├─ insQ.js
   │  ├─ insQ.min.js
   │  ├─ redoc
   │  │  ├─ LICENSE
   │  │  ├─ redoc-logo.png
   │  │  ├─ redoc.min.js
   │  │  └─ redoc.standalone.js.map
   │  ├─ redoc-init.js
   │  ├─ redoc-old
   │  │  ├─ LICENSE
   │  │  ├─ redoc.min.js
   │  │  └─ redoc.min.js.map
   │  ├─ style.css
   │  └─ swagger-ui-init.js
   └─ rest_framework
      ├─ css
      │  ├─ bootstrap-theme.min.css
      │  ├─ bootstrap-theme.min.css.map
      │  ├─ bootstrap-tweaks.css
      │  ├─ bootstrap.min.css
      │  ├─ bootstrap.min.css.map
      │  ├─ default.css
      │  ├─ font-awesome-4.0.3.css
      │  └─ prettify.css
      ├─ docs
      │  ├─ css
      │  │  ├─ base.css
      │  │  ├─ highlight.css
      │  │  └─ jquery.json-view.min.css
      │  ├─ img
      │  │  ├─ favicon.ico
      │  │  └─ grid.png
      │  └─ js
      │     ├─ api.js
      │     ├─ highlight.pack.js
      │     └─ jquery.json-view.min.js
      ├─ fonts
      │  ├─ fontawesome-webfont.eot
      │  ├─ fontawesome-webfont.svg
      │  ├─ fontawesome-webfont.ttf
      │  ├─ fontawesome-webfont.woff
      │  ├─ glyphicons-halflings-regular.eot
      │  ├─ glyphicons-halflings-regular.svg
      │  ├─ glyphicons-halflings-regular.ttf
      │  ├─ glyphicons-halflings-regular.woff
      │  └─ glyphicons-halflings-regular.woff2
      ├─ img
      │  ├─ glyphicons-halflings-white.png
      │  ├─ glyphicons-halflings.png
      │  └─ grid.png
      └─ js
         ├─ ajax-form.js
         ├─ bootstrap.min.js
         ├─ coreapi-0.1.1.js
         ├─ csrf.js
         ├─ default.js
         ├─ jquery-3.7.1.min.js
         ├─ load-ajax-form.js
         └─ prettify-min.js

``` -->