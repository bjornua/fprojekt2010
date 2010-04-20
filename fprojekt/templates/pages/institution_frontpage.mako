<%
    from random import randint
    count = 0
%>
<%inherit file="/subpage.mako"/>
<h1>${escape(name)}</h1>
<p>
    <a href=${esc_attr(url_for("institution_logout"))}>
        Log ud som institution
    </a>
</p>
<div id="inst_login">
<p>Klik på dit navn for at logge ind<p>
<table>
<tr>
% for user_name, user_email in users:
<% count += 1 %>
% if count % 4 == 1 and count != 1:
<tr></tr>
% endif
<td>
    <a href=${esc_attr(url_for("user_login",email=user_email))}><img height="100" src="/static/images/test-portræt.png" /></a><br />
    <a href=${esc_attr(url_for("user_login",email=user_email))}>${escape(user_name)}</a>
</td>
% endfor
</tr>
</table>
</div>

