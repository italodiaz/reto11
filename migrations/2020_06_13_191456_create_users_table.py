from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user') as table:
            table.increments('id')
            table.big_integer('user_id')
            table.string('name')
            table.string('email')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('user')
