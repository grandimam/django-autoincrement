# Django AutoIncrementField

Django Autoincrement for non-primary key fields

## Create Sequences

To create sequences for `AutoIncrementField`, run:

```commandline
python manage.py create_sequences --sequence-names <mymodel_sequence_name>
```

## Multiple Sequences

To create multiple sequences for `AutoIncrementField`, run:

```commandline
python manage.py create_sequences --sequence-names seq1 seq2 seq3
```