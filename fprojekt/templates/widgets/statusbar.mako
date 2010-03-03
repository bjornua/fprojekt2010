## -*- coding: utf-8 -*-
<div id="statusbar">
% if is_logged_in:
    <p>
        Du er logget ind som <a href="${url_for("user_profile")}">${name}</a>
    </p>
    <ul>
        <li><a href="${url_for("user_profile")}">Profil side</a>.</li>
        <li><a href="${url_for("user_logout")}">Log ud</a>.</li>
    </ul>
% else:
    <p>
        <a href="${url_for("user_register")}">
            Klik her for at tilmelde dig DIKULAN April 2010
        </a>
    </p>
% endif
</div>
