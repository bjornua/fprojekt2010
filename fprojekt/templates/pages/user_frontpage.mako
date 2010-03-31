<%inherit file="/main_user.mako"/>

<table>
    <thead>
        <tr>
            <th>Titel</th>
            <th>Oprettet</th>
            <th>Sidst rettet</th>
            <th>Antal ord</th>
    </thead>
    <tbody>
% for id, title, creation_date, modification_date, wordcount in documents:
        <tr class="document_row">
            <td><a href="${url_for("documentation_print",id=id)}">${title}</a></td>
            <td>${creation_date.day}/${creation_date.month}-${creation_date.year}</td>
            <td>${modification_date.day}/${modification_date.month}-${modification_date.year}</td>
            <td>${wordcount}</td>
        </tr>
% endfor
    </tbody>
</table>

<script type="text/javascript">
$(".document_row").css("cursor","pointer");
$(".document_row").mouseover(function () {
    $(this).css("background-color","#CCC");
});
$(".document_row").click(function () {
    window.location = $("a",this).attr("href");
});
$(".document_row").mouseout(function () {
    $(this).css("background-color","transparent");
});
</script>
