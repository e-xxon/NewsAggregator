<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.css"></link>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.12/semantic.min.js"></script>
    </head>
    <body>
        <div class="ui container" style="padding-top: 10px;">
        <table class="ui celled table">
            <thead>
                <th>Title</th>
                <th>OP</th>
                <th>Rating</th>
                <th>Comments</th>
                <th colspan="3">Label</th>
            </thead>
            <tbody>
                %for testnews,labels in rows:
                <tr>
                    <td><a href="{{ testnews.url }}">{{ testnews.title }}: {{labels.capitalize()}}</a></td>
                    <td>{{ testnews.author }}</td>
                    <td>{{ testnews.points }}</td>
                    <td>{{ testnews.comments }}</td>
                    <td class="positive"><a href="/add_label/?label=good&id={{ testnews.id }}">Круто</a></td>
                    <td class="active"><a href="/add_label/?label=maybe&id={{ testnews.id }}">Мэйби</a></td>
                    <td class="negative"><a href="/add_label/?label=never&id={{ testnews.id }}">Неочень</a></td>
                </tr>
                %end
            </tbody>
            <tfoot class="full-width">
                <tr>
                    <th colspan="7">
                        <a href="/update" class="ui right floated small primary button">Кнопка, которую ты не нажмешь</a>
                    </th>
                </tr>
            </tfoot>
        </table>
        </div>
    </body>
</html>
