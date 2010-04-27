## -*- coding: utf-8 -*-
<div id="topmenu">
    <h1 id="logotext" style="float:left;">
        PædagogNet
    </h1>
    <ul id="main-navigation">

% if active_section == "documentation":
        <li><a id="link-documentation" class="topmenu-active" href="${url_for("user_frontpage")}">Dokumentation</a></li>
% else:
        <li><a id="link-documentation" href="${url_for("user_frontpage")}">Dokumentation</a></li>
% endif
% if active_section == "curriculum":
        <li><a id="link-curriculum" class="topmenu-active" href="${url_for("curriculum_frontpage")}">Læreplaner</a></li>
% else:
        <li><a id="link-curriculum" href="${url_for("curriculum_frontpage")}">Læreplaner</a></li>
% endif
% if active_section == "evaluation":
        <li><a id="link-evaluation" class="topmenu-active" href="${url_for("evaluation_frontpage")}">Evaluering</a></li>
% else:
        <li><a id="link-evaluation" href="${url_for("evaluation_frontpage")}">Evaluering</a></li>
% endif
% if active_section == "other":
        <li><a id="link-other" class="topmenu-active" href="${url_for("admin_frontpage")}">Andet</a></li>
% else:
        <li><a id="link-other" href="${url_for("admin_frontpage")}">Andet</a></li>
% endif
    </ul>
</div>


