<%inherit file="/main_user.mako"/>

<table id="document_table">
    <thead>
        <tr id="document_row_header">
            <th class="document_col_title">Titel</th>
            <th class="document_col_created">Oprettet</th>
            <th class="document_col_modified">Sidst rettet</th>
            <th class="document_col_word_count">Antal ord</th>
        </tr>
    </thead>
    <tbody>
% for id, title, creation_date, modification_date, wordcount in documents:
        <tr class="document_row">
            <td class="document_col_title"><a href="${url_for("documentation_print",id=id)}">${title}</a></td>
            <td class="document_col_created">${creation_date.day}/${creation_date.month}-${creation_date.year}</td>
            <td class="document_col_modified">${modification_date.day}/${modification_date.month}-${modification_date.year}</td>
            <td class="document_col_word_count">${wordcount}</td>
        </tr>
% endfor
    </tbody>
</table>

<script type="text/javascript">
$(".document_row").click(function () {
    window.location = $("a",this).attr("href");
});
</script>
