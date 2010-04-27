<%inherit file="/subpage.mako"/>
<%!
    def title(kwargs):
        return "Fejl"
    def section(kwargs):
        return "other"
%>
<%
    response.status_code = 500
%>
<h1>Fejl</h1>
<p>
    Der skete en fejl på siden, vi er på sagen.
</p>
