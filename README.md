# RSS reader

RSS reader checks your feeds and sends an email which contains latests feeds' posts.

## Configuration

`config.json` contains confguration's settings.

| Name                    | Type            | Description                                                                                         | Example                                                              |
| ----------------------- | --------------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `feeds`                 | `Array<string>` | Feeds' urls                                                                                         | `["https://testfeeds.com/rss.xml","https://testfeeds2.com/rss.xml"]` |
| `period`                | `string`        | Period of last published feed's post.<br><br>`d` since yesterday<br>`w` last week<br>`m` last month | `"d"`                                                                |
| `feeds-email-recipient` | `string`        | Email's recipient                                                                                   | `"test@test.com"`                                                    |
| `smtp-host`             | `string`        | Smtp server's address                                                                               | `"smtp.test.com"`                                                    |
| `smtp-port`             | `integer`       | Smtp server's port                                                                                  | `465`                                                                |
| `smtp-user`             | `string`        | Smtp server's username                                                                              | `"user@test.com"`                                                    |
| `smtp-password`         | `string`        | Smtp server's password                                                                              | `"qwerty12356"`                                                      |

## Run

```
python ./rss_reader.py
```

## Libraries

-   [feedparser](https://feedparser.readthedocs.io/en/latest/)

```
pip install feedparser --user
```
