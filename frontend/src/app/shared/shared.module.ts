import {NgModule} from '@angular/core';
import {CommonModule} from "@angular/common";
import {RouterModule} from "@angular/router";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpModule} from "@angular/http";
import {
    MdButtonModule, MdCardModule, MdIconModule, MdInputModule, MdListModule, MdSidenavModule, MdToolbarModule,
    MdTooltipModule, MdProgressBarModule, MdSlideToggleModule, MdDialogModule, MdMenuModule, MdSliderModule,
    MdTabsModule, MdCheckboxModule, MdRadioModule, MdChipsModule, MdDatepickerModule, MdNativeDateModule, MdTableModule,
    MdCoreModule, MdSortModule, MdPaginatorModule
} from "@angular/material";
import {CdkTableModule} from "@angular/cdk";
import {BoardService} from "./board.service";
import {FlexLayoutModule} from "@angular/flex-layout";

@NgModule({
    imports: [
        // Angular Modules
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule,
        HttpModule,
        FlexLayoutModule,
        // Material Modules
        MdTooltipModule,
        MdButtonModule,
        MdCardModule,
        MdDialogModule,
        MdInputModule,
        MdSidenavModule,
        MdToolbarModule,
        MdIconModule,
        MdListModule,
        MdProgressBarModule,
        MdSlideToggleModule,
        MdMenuModule,
        MdSliderModule,
        MdTabsModule,
        MdCheckboxModule,
        MdRadioModule,
        MdChipsModule,
        MdDatepickerModule,
        MdNativeDateModule,
        MdTableModule,
        CdkTableModule,
        MdCoreModule,
        MdSortModule,
        MdPaginatorModule,
    ],
    exports: [
        // Angular Modules
        CommonModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule,
        HttpModule,
        // Flex Layout
        FlexLayoutModule,
        // Material Modules
        MdTooltipModule,
        MdButtonModule,
        MdCardModule,
        MdDialogModule,
        MdInputModule,
        MdSidenavModule,
        MdToolbarModule,
        MdIconModule,
        MdListModule,
        MdProgressBarModule,
        MdSlideToggleModule,
        MdMenuModule,
        MdSliderModule,
        MdSliderModule,
        MdTabsModule,
        MdCheckboxModule,
        MdRadioModule,
        MdChipsModule,
        MdDatepickerModule,
        MdNativeDateModule,
        MdTableModule,
        CdkTableModule,
        MdCoreModule,
        MdSortModule,
    ],
    declarations: [],
    providers: [
        BoardService
    ],
    entryComponents: []
})
export class SharedModule {
}
