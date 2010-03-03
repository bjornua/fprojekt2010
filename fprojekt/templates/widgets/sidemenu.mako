<li><a href="${url_for("frontpage")}">Forside</a></li>
<li><a href="${url_for("information")}">Information</a>
    <ul>
        <li><a href="${url_for("foodoptions")}">Madmuligheder</a></li>
        <li><a href="${url_for("tournaments_events")}">Turneringer/events</a></li>
        <li><a href="${url_for("rules")}">Regler</a></li>
    </ul>
</li>
<li><a href="${url_for("seatbooking")}">Pladsreservation</a></li>
<li><a href="${url_for("gallery")}">Galleri</a></li>
<li><a href="${url_for("contact")}">Kontakt</a></li>
% if is_logged_in:
    <li><a href="${url_for("user_logout")}">Log ud</a></li>
% else:
    <li><a href="${url_for("user_login")}">Log ind</a></li>
    <li><a href="${url_for("user_register")}">Tilmeld dig dikulan!</a></li>
% endif

