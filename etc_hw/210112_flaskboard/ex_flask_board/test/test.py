with recursive cte as
(
select  board_content_id,
        board_content_pid,
        member_id,
        board_content_title,
        board_content_body,
        board_content_regdatetime,
        board_content_edtdatetime,
        board_content_deleted,
        0 AS depth,
        CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as grp,
        CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as lvl
from    board
where   board_content_pid = -1 and board_id = :board_id
union all
select  r.board_content_id,
        r.board_content_pid,
        r.member_id,
        r.board_content_title,
        r.board_content_body,
        r.board_content_regdatetime,
        r.board_content_edtdatetime,
        r.board_content_deleted,
        depth + 1 AS depth,
        grp AS grp,
        CONCAT(cte.lvl, "-", LPAD(r.board_content_id, 10, "0")) as lvl
from    board r
inner join cte
        on r.board_content_pid = cte.board_content_id
)
SELECT * FROM
(SELECT * FROM
(SELECT @ROWNUM:=@ROWNUM+1 AS board_content_num, c.* 
FROM cte c, 
(SELECT @ROWNUM:=0) b ORDER BY CAST(board_content_id AS INTEGER)) t 
) a 
inner join member
on a.member_id = member.member_id
ORDER BY grp DESC, lvl
LIMIT :startrow, :numberInPage