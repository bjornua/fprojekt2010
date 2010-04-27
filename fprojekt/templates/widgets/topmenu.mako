## -*- coding: utf-8 -*-
<%
    links = (
        (u"Dokumentation", "documentation", url_for("user_frontpage")),
        (u"Læreplaner"   , "curriculum"   , url_for("curriculum_frontpage")),
        (u"Evaluation"   , "evaluation"   , url_for("evaluation_frontpage")),
        (u"Andet"        , "other"        , url_for("admin_frontpage")),
    )
%>
<div id="topmenu">
    <h1 id="logotext" style="float:left;">
        PædagogNet
    </h1>
    <ul id="main-navigation">
% for name, section, link in links:
        <li><a id="link-${section}" ${active_section == section and 'class="topmenu-active" ' or ""}href="${link}">${name}</a></li>
% endfor
    </ul>
</div>


