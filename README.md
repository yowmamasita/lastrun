# lastrun
Record the date and time a program was last run

`pip install lastrun`

## Methods

### when()

Returns last recorded time (`datetime.datetime`)

### record()

Record time (returns current time `now()`) (`datetime.datetime`)

### recorder(first_run_log, last_run_log, printer)

Returns last recorded time then records new run time (`datetime.timedelta`)
