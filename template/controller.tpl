package {{base_package}}.controller;

import {{base_package}}.pojo.po.{{domain | capitalize}};
import {{base_package}}.service.impl.{{domain | capitalize}}ServiceImpl;
import {{base_package}}.utils.request.SmeRequest;
import {{base_package}}.utils.response.SmeResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class {{domain | capitalize}}Controller {

    @Autowired
    private {{domain | capitalize}}ServiceImpl {{domain}}Service;

    @PostMapping("/{{domain}}")
    public SmeResponse<Long> create(@RequestBody SmeRequest<{{domain | capitalize}}> request) {
        return SmeResponse.ok({{domain}}Service.create(request.getRequestData()));
    }

    @DeleteMapping("/{{domain}}/{id}")
    public SmeResponse delete(@PathVariable("id") String id) {
        {{domain}}Service.deleteById(Long.parseLong(id));
        return SmeResponse.ok();
    }

    @PutMapping("/{{domain}}")
    public SmeResponse update(@RequestBody SmeRequest<{{domain | capitalize}}> request) {
        {{domain}}Service.update(request.getRequestData());
        return SmeResponse.ok();
    }

    @GetMapping("/{{domain}}/{id}")
    public SmeResponse<{{domain | capitalize}}> findById(@PathVariable("id") String id) {
        return SmeResponse.ok({{domain}}Service.findById(Long.parseLong(id)));
    }
}