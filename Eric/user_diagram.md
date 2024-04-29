@startuml
!theme plain

left to right direction

actor User as user 

package components as "Components" {
  usecase perform_scans as "Perform Scans"
  user -- perform_scans 
  
  usecase scan_subnets as "Scan Subnets"
  perform_scans <-[dashed]- scan_subnets : <<includes>>
  
  usecase scan_system as "Scan System"
  perform_scans <-[dashed]- scan_system : <<includes>>
  
  usecase display_network as "Display Network Topology"
  user -- display_network
  
  usecase view_vulnerabilities as "View System Vulnerabilities"
  user -- view_vulnerabilities
  
  usecase run_exploit as "Run Exploit"
  user -- run_exploit
}
@enduml
