import {Component} from '@angular/core';
import {NavigationEnd, Router} from "@angular/router";
import {Subscription} from "rxjs/Subscription";
import {ROUTES} from "./app.routes";
import 'rxjs/add/operator/filter';

@Component({
    selector: 'app',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss']
})
export class AppComponent {
    public menuItems: any[];

    private routerSub: Subscription;

    constructor(private router: Router) {
        // get all routes
        this.menuItems = ROUTES.map((route) => {
            return {
                name: route.component && route.data.title,
                route: route.path
            };
        }).slice(0, ROUTES.length - 1);
    }

    ngOnInit() {
        this.routerSub = this.router.events.filter((event) => event instanceof NavigationEnd).subscribe((event) => {
            window.scrollTo(0, 0);
        })
    }

    ngOnDestroy() {
        this.routerSub.unsubscribe();
    }
}
