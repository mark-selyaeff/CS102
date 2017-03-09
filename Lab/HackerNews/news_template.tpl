<div><a href="/train">Train!</a></div>
<table border=1>
    <tr>
        <th>Title</th>
        <th>Author</th>
        <th>#likes</th>
        <th>#comments</th>
        <th colspan="3">Label</th>
    <tr>
        <td>Интересные: ---></td>
    </tr>
    </tr>
    %for row in rows_good:
        <tr>
            <td><a href="http://{{row.url}}">{{row.title}}</a></td>
            <td>{{row.author}}</td>
            <td>{{row.points}}</td>
            <td>{{row.comments}}</td>
            <td><a href="/add_label?label=good&id={{row.id}}">Интересно</a></td>
            <td><a href="/add_label?label=maybe&id={{row.id}}">Возможно</a></td>
            <td><a href="/add_label?label=never&id={{row.id}}">Не интересно</a></td>
        </tr>
    %end
    <tr><td>Возможно интересные ---></td></tr>
    %for row in rows_maybe:
        <tr>
            <td><a href="http://{{row.url}}">{{row.title}}</a></td>
            <td>{{row.author}}</td>
            <td>{{row.points}}</td>
            <td>{{row.comments}}</td>
            <td><a href="/add_label?label=good&id={{row.id}}">Интересно</a></td>
            <td><a href="/add_label?label=maybe&id={{row.id}}">Возможно</a></td>
            <td><a href="/add_label?label=never&id={{row.id}}">Не интересно</a></td>
        </tr>
    %end
    <tr>
        <td>Неинтересные ---></td>
    </tr>
    %for row in rows_never:
        <tr>
            <td><a href="http://{{row.url}}">{{row.title}}</a></td>
            <td>{{row.author}}</td>
            <td>{{row.points}}</td>
            <td>{{row.comments}}</td>
            <td><a href="/add_label?label=good&id={{row.id}}">Интересно</a></td>
            <td><a href="/add_label?label=maybe&id={{row.id}}">Возможно</a></td>
            <td><a href="/add_label?label=never&id={{row.id}}">Не интересно</a></td>
        </tr>
    %end
</table>
<div style="background: green; color: white"><a href="/update_news">I Wanna more HACKER NEWS!</a></div>