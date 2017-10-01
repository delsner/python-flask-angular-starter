import {Injectable} from '@angular/core';
import {Http} from "@angular/http";
import {Observable} from "rxjs/Observable";
import {Board} from "./board.type";
import 'rxjs/add/operator/map';

@Injectable()
export class BoardService {

    private SERVER_URL: string = 'api/';

    constructor(private http: Http) {
    }

    public getAllBoards(): Observable<Board[]> {
        return this.http.get(this.SERVER_URL + 'board').map((res) => res.json());
    }

    public getSingleBoard(board: Board): Observable<Board> {
        return this.http.get(this.SERVER_URL + `board/${board.id}`).map((res) => res.json());
    }

    public createBoard(board: Board): Observable<Board> {
        return this.http.post(this.SERVER_URL + `board`, board).map((res) => res.json());
    }
}
