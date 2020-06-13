from orator.migrations import Migration


class CreateMessageTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('message') as table:
            table.increments('id')
            table.string('message')
            table.string('message_id')
            table.integer('id_user').references('id').on('user')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('message')
