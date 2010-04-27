<%inherit file="/subpage.mako"/>
<%!
    def title(kwargs):
        return "Siden blev ikke fundet"
    def section(kwargs):
        return "other"
%>
<%
    response.status_code = 404
%>
<h1>Ukendt side.</h1>
<p>
    Siden blev ikke fundet.
    
    <a href=${esc_attr(url_for("index"))}>Gå til forsiden</a>
</p>
