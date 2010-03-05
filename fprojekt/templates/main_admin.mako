<%inherit file="/main.mako"/>
<ul>
    <li><a href="${url_for("admin_frontpage")}">Administration panel</a></li>
    <li><a href="${url_for("institution_list")}">Institutionsliste</a>
    <li><a href="${url_for("institution_create")}">Opret institution</a></li>
</ul>
<hr>
${next.body()}

