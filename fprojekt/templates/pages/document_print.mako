<%inherit file="/subpage.mako"/>
<h1>${escape(document_title)}</h1>
<p>
    Skrevet af ${escape(user_name)}
    &lt;<a href=${esc_attr("mailto:" + user_email)}>${escape(user_email)}</a>&gt;
    d. ${document_modified.day}/${document_modified.month}-${document_modified.year}
</p>

% for id, title, content in document_sections:
    <h3>${escape(title)}</h3>
    ${content}
% endfor
