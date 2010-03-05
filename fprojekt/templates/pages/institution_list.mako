<%inherit file="/main_admin.mako"/>
<h1>Institutioner</h1>
<ul>
    <li>
        <a href="${url_for("institution_create")}">Opret institution</a>
    </li>
</ul>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Email</th>
            <th>Phone</th>
        </tr>
    </thead>
    <tbody>
% for entry in entries:
    <tr>
        <td><a href="${url_for("institution_modify",id=entry[0])}">${entry[1]}</td>
        <td><a href="mailto:${entry[2]}">${escape(entry[2])}</a></td>
        <td>${escape(entry[3])}</td>
    </tr>
% endfor
    </tbody>
</table>
