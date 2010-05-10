## -*- coding: utf-8 -*-
<%
    links = (
        ("documentation", u"Dokumentation", url_for("user_frontpage"      )),
        ("curriculum"   , u"Læreplaner"   , url_for("curriculum_frontpage")),
        ("evaluation"   , u"Evaluering"   , url_for("evaluation_frontpage")),
        ("other"        , u"Andet"        , url_for("admin_frontpage"     )),
        ("logout"       , u"Log ud"       , url_for("user_logout"         )),
    )
%>
<div id="topmenu">
    <img src="/static/images/logo.png" alt="PædagogNET" id="logo-img" />
    <h1 id="section-header" class="${active_section}">
        <img src="/static/images/icons/big/${active_section}.png" />
        ${[x[1] for x in links if x[0] == active_section][0]}
    </h1>
    <ul id="main-navigation">
% for link in links:
<%
    section, name, url = link
%>
        <li><a id="link-${section}" ${active_section == section and 'class="topmenu-active" ' or ""}href="${url}"></a></li>
% endfor
    </ul>
</div>
