from django.urls import path
from inventory.views import *

urlpatterns = [
    path('inventory-supplier/create', InventorySupplierCreateView.as_view(), name='inventory_supplier_create'),
    path('inventory-supplier/index', InventorySupplierListView.as_view(), name='inventory_supplier_index'),
    path('inventory-supplier/<int:pk>/detail', InventorySupplierDetailView.as_view(), name='inventory_supplier_detail'),
    path('inventory-supplier/<int:pk>/edit', InventorySupplierUpdateView.as_view(), name='inventory_supplier_edit'),
    path('inventory-supplier/<int:pk>/delete', InventorySupplierDeleteView.as_view(), name='inventory_supplier_delete'),

    path('inventory-category/create', InventoryCategoryCreateView.as_view(), name='inventory_category_create'),
    path('inventory-category/index', InventoryCategoryListView.as_view(), name='inventory_category_index'),
    path('inventory-category/<int:pk>/edit', InventoryCategoryUpdateView.as_view(), name='inventory_category_edit'),
    path('inventory-category/<int:pk>/delete', InventoryCategoryDeleteView.as_view(), name='inventory_category_delete'),

    path('inventory-item/create', InventoryItemCreateView.as_view(), name='inventory_item_create'),
    path('inventory-item/index', InventoryItemListView.as_view(), name='inventory_item_index'),
    path('inventory-item/<int:pk>/detail', InventoryItemDetailView.as_view(), name='inventory_item_detail'),
    path('inventory-item/<int:pk>/edit', InventoryItemUpdateView.as_view(), name='inventory_item_edit'),
    path('inventory-item/<int:pk>/delete', InventoryItemDeleteView.as_view(), name='inventory_item_delete'),

    path('inventory-assign/create', InventoryAssignCreateView.as_view(), name='inventory_assign_create'),
    path('inventory-assign/index', InventoryAssignListView.as_view(), name='inventory_assign_index'),
    path('inventory-assign/<int:pk>/detail', InventoryAssignDetailView.as_view(), name='inventory_assign_detail'),
    path('inventory-assign/<int:pk>/edit', InventoryAssignUpdateView.as_view(), name='inventory_assign_edit'),
    path('inventory-assign/<int:pk>/delete', InventoryAssignDeleteView.as_view(), name='inventory_assign_delete'),

    path('inventory-stock/create', InventoryStockCreateView.as_view(), name='inventory_stock_create'),
    path('inventory-stock/index', InventoryStockListView.as_view(), name='inventory_stock_index'),
    path('inventory-stock/<int:pk>/delete', InventoryStockDeleteView.as_view(), name='inventory_stock_delete'),
    path('inventory-stock/<int:pk>/stock-out', stock_out_damaged_inventory, name='inventory_stock_out_damage'),

    path('inventory-stock-out/select-student', InventorySelectStudentView.as_view(), name='inventory_select_student'),
    path('inventory-stock-out/<int:pk>/collect', student_inventory_collect, name='inventory_student_collect'),
    path('inventory-stock-out/<int:pk>/bulk-collect', student_inventory_bulk_collect,
         name='inventory_student_bulk_collect'),

    path('inventory-stock-out/select-staff', inventory_staff_select, name='inventory_select_staff'),
    path('inventory-stock-out/<int:pk>/staff-bulk-collect', staff_inventory_bulk_collect,
         name='inventory_staff_bulk_collect'),
    path('inventory-stock-out/index', InventoryStockOutListView.as_view(), name='inventory_stock_out_index'),
    path('inventory-stock-out/<int:pk>/detail', InventoryStockOutDetailView.as_view(), name='inventory_stock_out_detail'),
    path('inventory-stock-out/<int:pk>/delete', InventoryStockOutDeleteView.as_view(), name='inventory_stock_out_delete'),

    path('asset-category/create', AssetCategoryCreateView.as_view(), name='asset_category_create'),
    path('asset-category/index', AssetCategoryListView.as_view(), name='asset_category_index'),
    path('asset-category/<int:pk>/edit', AssetCategoryUpdateView.as_view(), name='asset_category_edit'),
    path('asset-category/<int:pk>/delete', AssetCategoryDeleteView.as_view(), name='asset_category_delete'),

    path('asset/create', AssetCreateView.as_view(), name='asset_create'),
    path('asset/index', AssetListView.as_view(), name='asset_index'),
    path('asset/<int:pk>/detail', AssetDetailView.as_view(), name='asset_detail'),
    path('asset/<int:pk>/edit', AssetUpdateView.as_view(), name='asset_edit'),
    path('asset/<int:pk>/delete', AssetDeleteView.as_view(), name='asset_delete'),

    path('dashboard', InventoryDashboardView.as_view(), name='inventory_dashboard'),

]

