import {Component, OnInit} from '@angular/core';
import {BoardService} from "../../shared/board.service";
import {Board} from "../../shared/board.type";

@Component({
    selector: 'home',
    templateUrl: './home.component.html',
    styleUrls: []
})
export class HomeComponent implements OnInit {

    public boards: Board[] = [];
    public board: Board = new Board();

    constructor(private boardService: BoardService) {
        this.getAllBoards();
    }

    ngOnInit() {
    }

    public getAllBoards() {
        this.boardService.getAllBoards().subscribe((boards) => {
            this.boards = boards;
        });
    }

    public createBoard() {
        this.boardService.createBoard(this.board).subscribe((board) => {
            alert(`Created board with name ${board.name}`);
            this.getAllBoards();
            this.board = new Board();
        });
    }

}
