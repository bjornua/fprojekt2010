<%inherit file="/subpage.mako"/>
<%!
    def title(self):
        return "Administration"
    def section(self):
        return "other"
%>
<h1>Administrations panel</h1>
<p>
<a href="${url_for("institution_list")}">Institutionsliste</a>
</p>
