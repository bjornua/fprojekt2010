<%inherit file="/main_admin.mako"/>
<h1>Institution: ${escape(db_name)} (${escape(db_email)})</h1>
<p>
    <a href="${url_for("institution_list")}">Tilbage til liste</a>
</p>
<form action="${url_for("institution_modify",id=id)}" method="post">
    <label for="id">Nr.:</label><br/>
    <input id="id" type="text" value="${id}" disabled="disabled"/><br/>
    
    <label for="name">Navn:</label><br/>
    <input type="text" id="name" value=${esc_attr(name)} name="name"/><br/>
    
    <label for="email">Email:</label><br/>
    <input type="text" id="email" value=${esc_attr(email)} name="email"/><br/>
    
    <label for="phone">Telefon:</label><br/>
    <input type="text" id="phone" value=${esc_attr(phone)} name="phone"/><br/>

    <label for="phone">Password:</label><br/>
    <input type="text" id="password" value=${esc_attr(password)} name="password"/><br/>
    
    <input type="submit" value="Gem ændringer"/>
    
    </table>
</form>
<p>
    <a href="${url_for("institution_delete",id=id)}">Slet bruger</a>
</p>
<h3>Brugere</h3>
<ul>
    <li>
        <a href="${url_for("user_create",inst_id=id)}">Opret bruger</a>
    </li>
</ul>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Email</th>
        </tr>
    </thead>
    <tbody>
% for entry in entries:
    <tr>
        <td><a href="${url_for("user_modify",id=entry[0])}">${entry[1]}</td>
        <td><a href="mailto:${entry[2]}">${escape(entry[2])}</a></td>
    </tr>
% endfor
    </tbody>
</table>
