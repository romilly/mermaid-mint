PROCESS = """
process:
  process_id: "user_registration"
  name: "User Registration Process"
  
steps:
  - step_id: "start"
    type: "Start"
    name: "Begin Registration"
    successor: "validate_email"
    
  - step_id: "validate_email"
    type: "Task"
    name: "Validate Email Address"
    successor: "check_existing_user"
    
  - step_id: "check_existing_user"
    type: "Decision"
    name: "Check if User Exists"
    test: "user_exists == true"
    "yes": "reject_duplicate"
    "no": "create_account"
    
  - step_id: "reject_duplicate"
    type: "Task"
    name: "Reject Duplicate User"
    successor: "end_rejected"
    
  - step_id: "create_account"
    type: "Task"
    name: "Create User Account"
    successor: "send_confirmation"
    
  - step_id: "send_confirmation"
    type: "Task"
    name: "Send Confirmation Email"
    successor: "end_success"
    
  - step_id: "end_rejected"
    type: "End"
    name: "Registration Rejected"
    
  - step_id: "end_success"
    type: "End"
    name: "Registration Complete"
"""

PROCESS_WITH_RESOURCES = """
process:
  process_id: "order_processing"
  name: "Order Processing Workflow"
  
steps:
  - step_id: "start"
    type: "Start"
    name: "Begin Order Processing"
    successor: "save_order"
    
  - step_id: "save_order"
    type: "Task"
    name: "Save Order Details"
    operations:
      - type: "Update"
        target: "orders_db"
        description: "Insert new order record"
      - type: "Update"
        target: "audit_log"
        description: "Log order creation event"
    successor: "check_inventory"
    
  - step_id: "check_inventory"
    type: "Decision"
    name: "Check Product Availability"
    test:
      type: "Query"
      target: "inventory_db"
      description: "Check if product is in stock"
    "yes": "process_payment"
    "no": "backorder"
    
  - step_id: "process_payment"
    type: "Task"
    name: "Process Payment"
    operations:
      - type: "Update"
        target: "payment_db"
        description: "Record payment transaction"
    successor: "end_success"
    
  - step_id: "backorder"
    type: "Task"
    name: "Create Backorder"
    operations:
      - type: "Update"
        target: "orders_db"
        description: "Mark order as backordered"
      - type: "Update"
        target: "notification_doc"
        description: "Generate customer notification"
    successor: "end_backorder"
    
  - step_id: "orders_db"
    type: "Database"
    name: "Orders Database"
    
  - step_id: "inventory_db"
    type: "Database"
    name: "Inventory Database"
    
  - step_id: "payment_db"
    type: "Database"
    name: "Payment Database"
    
  - step_id: "audit_log"
    type: "Document"
    name: "Audit Log"
    
  - step_id: "notification_doc"
    type: "Document"
    name: "Customer Notification"
    
  - step_id: "end_success"
    type: "End"
    name: "Order Processed Successfully"
    
  - step_id: "end_backorder"
    type: "End"
    name: "Order Backordered"
"""