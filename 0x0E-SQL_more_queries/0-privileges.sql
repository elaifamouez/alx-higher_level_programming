-- Check MySQL version
SELECT VERSION();

-- List privileges for user_0d_1 and user_0d_2
SELECT
    USER AS 'User',
    HOST AS 'Host',
    IFNULL(SELECT_PRIV, '') AS 'Select_priv',
    IFNULL(INSERT_PRIV, '') AS 'Insert_priv',
    IFNULL(UPDATE_PRIV, '') AS 'Update_priv',
    IFNULL(DELETE_PRIV, '') AS 'Delete_priv',
    IFNULL(CREATE_PRIV, '') AS 'Create_priv',
    IFNULL(DROP_PRIV, '') AS 'Drop_priv',
    IFNULL(GRANT_PRIV, '') AS 'Grant_priv',
    IFNULL(REFERENCES_PRIV, '') AS 'References_priv',
    IFNULL(INDEX_PRIV, '') AS 'Index_priv',
    IFNULL(ALTER_PRIV, '') AS 'Alter_priv',
    IFNULL(CREATE_TMP_TABLE_PRIV, '') AS 'Create_tmp_table_priv',
    IFNULL(LOCK_TABLES_PRIV, '') AS 'Lock_tables_priv',
    IFNULL(CREATE_VIEW_PRIV, '') AS 'Create_view_priv',
    IFNULL(SHOW_VIEW_PRIV, '') AS 'Show_view_priv',
    IFNULL(CREATE_ROUTINE_PRIV, '') AS 'Create_routine_priv',
    IFNULL(ALTER_ROUTINE_PRIV, '') AS 'Alter_routine_priv',
    IFNULL(EXECUTE_PRIV, '') AS 'Execute_priv',
    IFNULL(EVENT_PRIV, '') AS 'Event_priv',
    IFNULL(TRIGGER_PRIV, '') AS 'Trigger_priv'
FROM
    information_schema.USER_PRIVILEGES
WHERE
    USER IN ('user_0d_1', 'user_0d_2')
    AND HOST = 'localhost';
